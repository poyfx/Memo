<script setup lang="ts">
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import MemoEmptyState from "../components/MemoEmptyState.vue";
import MemoForm from "../components/MemoForm.vue";
import MemoListItem from "../components/MemoListItem.vue";
import { useMemoStore } from "../stores/memo";

const store = useMemoStore();
const { memos, loading, error, pendingCount, doneCount } = storeToRefs(store);

onMounted(() => {
  if (!store.loaded) {
    void store.refreshMemos();
  }
});

function handleCreate(payload: { title: string; remind_at: string | null }) {
  void store.addMemo(payload);
}
</script>

<template>
  <section class="page">
    <div class="grid grid--2">
      <div class="panel">
        <h2 class="panel__title">新增备忘录</h2>
        <p class="panel__desc">后面这里会直接对接 FastAPI。</p>
        <MemoForm @submit="handleCreate" />
      </div>

      <div class="grid">
        <div class="panel kpi">
          <span class="kpi__label">待完成</span>
          <strong class="kpi__value">{{ pendingCount }}</strong>
        </div>
        <div class="panel kpi">
          <span class="kpi__label">已完成</span>
          <strong class="kpi__value">{{ doneCount }}</strong>
        </div>
      </div>
    </div>

    <div class="panel">
      <h2 class="panel__title">备忘录列表</h2>
      <p v-if="error" class="panel__desc">{{ error }}</p>
      <p v-else-if="loading" class="panel__desc">加载中...</p>
      <MemoEmptyState v-else-if="memos.length === 0" />
      <div v-else class="memo-list">
        <MemoListItem
          v-for="memo in memos"
          :key="memo.id"
          :memo="memo"
          @toggle="store.toggleMemoDone"
          @remove="store.removeMemo"
        />
      </div>
    </div>
  </section>
</template>
