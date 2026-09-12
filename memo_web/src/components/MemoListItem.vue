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

<style scoped>
.memo-item {
  display: grid;
  gap: 10px;
  padding: 18px;
  border-radius: 18px;
  background: rgba(0, 0, 0, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.memo-item__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.memo-item__title {
  margin: 0;
  font-size: 16px;
}

.memo-item.is-done .memo-item__title {
  text-decoration: line-through;
  opacity: 0.62;
}

.memo-item__meta {
  color: var(--text-subtle);
  font-size: 13px;
}

.memo-item__actions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.badge {
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(240, 179, 106, 0.12);
  color: var(--brand-strong);
  font-size: 13px;
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

.button--ghost {
  background: rgba(255, 255, 255, 0.07);
  color: var(--text-main);
}

.button--danger {
  background: rgba(235, 116, 98, 0.18);
  color: #ffb0a4;
}
</style>
