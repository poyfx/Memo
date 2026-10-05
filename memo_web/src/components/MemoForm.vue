<script setup lang="ts">
import { reactive } from "vue";

const emit = defineEmits<{
  submit: [payload: { title: string; remind_at: string | null }];
}>();

const form = reactive({
  title: "",
  remind_at: "",
});

function handleSubmit() {
  const title = form.title.trim();
  if (!title) return;

  emit("submit", {
    title,
    remind_at: form.remind_at || null,
  });

  form.title = "";
  form.remind_at = "";
}
</script>

<template>
  <form class="memo-form" @submit.prevent="handleSubmit">
    <el-input
      v-model="form.title"
      size="large"
      placeholder="备忘录标题"
      clearable
    />

    <div class="memo-form__row">
      <el-date-picker
        v-model="form.remind_at"
        type="datetime"
        value-format="YYYY-MM-DDTHH:mm"
        placeholder="选择提醒时间"
        size="large"
        clearable
      />
    </div>

    <el-button type="primary" size="large" native-type="submit">
      新增备忘录
    </el-button>
  </form>
</template>

<style scoped>
.memo-form {
  display: grid;
  gap: 14px;
}

.memo-form__row {
  display: grid;
  gap: 12px;
}

</style>
