import { defineStore } from "pinia";
import { computed, ref } from "vue";
import {
  createMemo,
  deleteMemo,
  listMemos,
  updateMemo,
  updateMemoDone,
} from "../api/memo";
import type { Memo } from "../types/memo";

export const useMemoStore = defineStore("memo", () => {
  const memos = ref<Memo[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);
  const loaded = ref(false);

  const pendingCount = computed(
    () => memos.value.filter((memo) => !memo.done).length,
  );
  const doneCount = computed(() => memos.value.filter((memo) => memo.done).length);

  async function refreshMemos() {
    loading.value = true;
    error.value = null;

    try {
      memos.value = await listMemos();
      loaded.value = true;
    } catch (err) {
      error.value = err instanceof Error ? err.message : "加载失败";
    } finally {
      loading.value = false;
    }
  }

  async function addMemo(payload: { title: string; remind_at: string | null }) {
    const memo = await createMemo(payload);
    memos.value.unshift(memo);
  }

  async function editMemo(
    memoId: number,
    payload: Partial<Pick<Memo, "title" | "done" | "remind_at">>,
  ) {
    const updated = await updateMemo(memoId, payload);
    memos.value = memos.value.map((memo) => (memo.id === memoId ? updated : memo));
  }

  async function toggleMemoDone(memoId: number) {
    const current = memos.value.find((memo) => memo.id === memoId);
    if (!current) return;

    const updated = await updateMemoDone(memoId, !current.done);
    memos.value = memos.value.map((memo) => (memo.id === memoId ? updated : memo));
  }

  async function removeMemo(memoId: number) {
    await deleteMemo(memoId);
    memos.value = memos.value.filter((memo) => memo.id !== memoId);
  }

  return {
    memos,
    loading,
    error,
    loaded,
    pendingCount,
    doneCount,
    refreshMemos,
    addMemo,
    editMemo,
    toggleMemoDone,
    removeMemo,
  };
});
