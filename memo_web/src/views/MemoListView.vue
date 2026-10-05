<script setup lang="ts">
import { onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { ElMessage, ElMessageBox } from "element-plus";
import { EditPen } from "@element-plus/icons-vue";
import MemoForm from "../components/MemoForm.vue";
import MemoListItem from "../components/MemoListItem.vue";
import { useMemoStore } from "../stores/memo";

const store = useMemoStore();
const { memos, loading, error, pendingCount, doneCount } = storeToRefs(store);
const removingId = ref<number | null>(null);

onMounted(() => {
  if (!store.loaded) {
    void store.refreshMemos();
  }
});

function handleCreate(payload: { title: string; remind_at: string | null }) {
  void store.addMemo(payload);
}

async function handleRemove(memoId: number) {
  const memo = memos.value.find((item) => item.id === memoId);
  if (!memo) return;

  try {
    await ElMessageBox.confirm(
      `确定删除“${memo.title}”吗？`,
      "删除备忘录",
      {
        confirmButtonText: "删除",
        cancelButtonText: "取消",
        type: "warning",
      },
    );
  } catch {
    return;
  }

  removingId.value = memoId;
  error.value = null;

  try {
    await store.removeMemo(memoId);
    ElMessage.success("备忘录已删除");
  } catch (err) {
    error.value = err instanceof Error ? err.message : "删除失败";
  } finally {
    removingId.value = null;
  }
}
</script>

<template>
  <section class="page">
    <div class="grid grid--2">
      <el-card class="surface" shadow="never">
        <template #header>
          <div class="card-heading">
            <div>
              <h2 class="panel__title">新增备忘录</h2>
              <p class="panel__desc">记录一件要完成的事情。</p>
            </div>
            <el-icon class="card-heading__icon"><EditPen /></el-icon>
          </div>
        </template>
        <MemoForm @submit="handleCreate" />
      </el-card>

      <div class="grid">
        <el-card class="surface stat-card" shadow="never">
          <el-statistic title="待完成" :value="pendingCount" />
        </el-card>
        <el-card class="surface stat-card" shadow="never">
          <el-statistic title="已完成" :value="doneCount" />
        </el-card>
      </div>
    </div>

    <el-card class="surface" shadow="never">
      <template #header>
        <div class="list-heading">
          <h2 class="panel__title">备忘录列表</h2>
          <el-tag effect="plain">{{ memos.length }} 条</el-tag>
        </div>
      </template>
      <el-alert v-if="error" :title="error" type="error" show-icon />
      <el-skeleton v-else-if="loading" :rows="4" animated />
      <el-empty v-else-if="memos.length === 0" description="还没有备忘录" />
      <div v-else class="memo-list">
        <MemoListItem
          v-for="memo in memos"
          :key="memo.id"
          :memo="memo"
          :removing="removingId === memo.id"
          @toggle="store.toggleMemoDone"
          @remove="handleRemove"
        />
      </div>
    </el-card>
  </section>
</template>

<style scoped>
.page {
  display: grid;
  gap: 20px;
}

.grid {
  display: grid;
  gap: 16px;
}

.grid--2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.panel {
  padding: 20px;
  border-radius: 20px;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}

.surface {
  border: 1px solid var(--border);
  background: rgba(28, 24, 22, 0.78);
}

.surface :deep(.el-card__header) {
  padding: 18px 20px;
  border-bottom-color: var(--border);
}

.surface :deep(.el-card__body) {
  padding: 20px;
}

.card-heading,
.list-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.card-heading__icon {
  color: var(--brand-strong);
  font-size: 22px;
}

.stat-card {
  min-height: 118px;
  display: flex;
  align-items: center;
}

.stat-card :deep(.el-statistic__head) {
  color: var(--text-subtle);
}

.stat-card :deep(.el-statistic__content) {
  color: var(--text-main);
  font-size: 30px;
  font-weight: 700;
}

.list-heading .panel__title {
  margin: 0;
}

.panel__title {
  margin: 0 0 10px;
  font-size: 18px;
}

.panel__desc {
  margin: 0;
  color: var(--text-subtle);
}

.memo-list {
  display: grid;
  gap: 12px;
}

.kpi {
  display: grid;
  gap: 6px;
}

.kpi__label {
  color: var(--text-subtle);
  font-size: 13px;
}

.kpi__value {
  font-size: 28px;
  font-weight: 700;
}

@media (max-width: 960px) {
  .grid--2 {
    grid-template-columns: 1fr;
  }
}
</style>
