<script setup lang="ts">
import type { Memo } from "../types/memo";
import { useRouter } from "vue-router";

const router = useRouter();

defineProps<{
  memo: Memo;
  removing?: boolean;
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

      <el-tag :type="memo.done ? 'success' : 'warning'" effect="plain">
        {{ memo.done ? "已完成" : "待办" }}
      </el-tag>
    </div>

    <div class="memo-item__actions">
      <el-button
        plain
        @click="router.push({ name: 'editor', query: { id: memo.id } })"
      >
        编辑
      </el-button>
      <el-button
        plain
        @click="emit('toggle', memo.id)"
      >
        {{ memo.done ? "撤销完成" : "标记完成" }}
      </el-button>
      
      <el-button
        type="danger"
        plain
        :disabled="removing"
        @click="emit('remove', memo.id)"
      >
        {{ removing ? "删除中..." : "删除" }}
      </el-button>
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

</style>
