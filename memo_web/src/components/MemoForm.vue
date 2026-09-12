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
    <input
      v-model="form.title"
      class="memo-form__input"
      placeholder="备忘录标题"
    />

    <div class="memo-form__row">
      <input
        v-model="form.remind_at"
        class="memo-form__input"
        type="datetime-local"
      />
      <textarea
        class="memo-form__textarea"
        placeholder="备注内容，后面可扩展"
      />
    </div>

    <button class="button" type="submit">新增备忘录</button>
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

.memo-form__input,
.memo-form__textarea {
  padding: 14px 16px;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-main);
}

.memo-form__textarea {
  min-height: 120px;
  resize: vertical;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 40px;
  padding: 0 14px;
  border-radius: 12px;
  background: var(--brand);
  color: #24170f;
  font-weight: 600;
  border: 0;
  cursor: pointer;
}
</style>
