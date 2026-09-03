<script setup lang="ts">
import type { Memo } from "../types/memo";

defineProps<{
  memo: Memo;
}>();

const emit = defineEmits<{
  toggle: [id: number];
  remove: [id: number];
}>();
</script>

<template>
  <article class="memo-item" :class="{ 'is-done': memo.done }">
    <div class="memo-item__head">
      <div>
        <h3 class="memo-item__title">{{ memo.title }}</h3>
        <p class="memo-item__meta">
          提醒时间：{{ memo.remind_at ?? "未设置" }}
        </p>
      </div>

      <span class="badge">{{ memo.done ? "已完成" : "待办" }}</span>
    </div>

    <div class="memo-item__actions">
      <button
        class="button button--ghost"
        type="button"
        @click="emit('toggle', memo.id)"
      >
        {{ memo.done ? "撤销完成" : "标记完成" }}
      </button>
      <button
        class="button button--danger"
        type="button"
        @click="emit('remove', memo.id)"
      >
        删除
      </button>
    </div>
  </article>
</template>
