<script setup lang="ts">
import { onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { getMemo, updateMemo } from "../api/memo";
import { useMemoStore } from "../stores/memo";

const route = useRoute();
const router = useRouter();
const memoStore = useMemoStore();

const loading = ref(false);
const saving = ref(false);
const error = ref<string | null>(null);

const form = reactive({
  title: "",
  remind_at: "",
  done: false,
});

const memoId = Number(route.query.id);
onMounted(async () => {
  if (!Number.isInteger(memoId)) {
    error.value = "缺少备忘录 id";
    return;
  }

  loading.value = true;

  try {
    const memo = await getMemo(memoId);

    form.title = memo.title;
    form.done = memo.done;
    form.remind_at = memo.remind_at
      ? memo.remind_at.slice(0, 16)
      : "";
  } catch (err) {
    error.value = err instanceof Error ? err.message : "加载失败";
  } finally {
    loading.value = false;
  }
});
async function handleSubmit() {
  saving.value = true;
  error.value = null;

  try {
    await updateMemo(memoId, {
      title: form.title,
      done: form.done,
      remind_at: form.remind_at
        ? `${form.remind_at}:00`
        : null,
    });

    await memoStore.refreshMemos();
    await router.push({ name: "memos" });
  } catch (err) {
    error.value = err instanceof Error ? err.message : "保存失败";
  } finally {
    saving.value = false;
  }
}
</script>
<template>
  <section class="page">
    <div class="panel">
      <h2 class="panel__title">编辑备忘录</h2>

      <p v-if="loading" class="panel__desc">加载中...</p>
      <p v-else-if="error" class="panel__desc">{{ error }}</p>

      <el-form
        v-else
        class="editor-form"
        label-position="top"
        @submit.prevent="handleSubmit"
      >
        <el-form-item label="标题">
          <el-input v-model="form.title" size="large" clearable />
        </el-form-item>

        <el-form-item label="提醒时间">
          <el-date-picker
            v-model="form.remind_at"
            type="datetime"
            value-format="YYYY-MM-DDTHH:mm"
            placeholder="选择提醒时间"
            size="large"
            clearable
          />
        </el-form-item>

        <el-checkbox v-model="form.done">已完成</el-checkbox>

        <div class="editor-actions">
          <el-button
            type="primary"
            native-type="submit"
            :loading="saving"
          >
            {{ saving ? "保存中..." : "保存修改" }}
          </el-button>
          <el-button
            plain
            @click="router.push({ name: 'memos' })"
          >
            取消
          </el-button>
        </div>
      </el-form>
    </div>
  </section>
</template>

<style scoped>
.page {
  display: grid;
  gap: 20px;
}

.panel {
  padding: 20px;
  border-radius: 20px;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}

.panel__title {
  margin: 0 0 10px;
  font-size: 18px;
}

.panel__desc {
  margin: 0;
  color: var(--text-subtle);
}

.editor-form {
  display: grid;
  gap: 18px;
}

.editor-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
</style>
