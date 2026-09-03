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
