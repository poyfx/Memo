import type { Memo } from "../types/memo";
import { requestJson } from "./http";

export function listMemos() {
  return requestJson<Memo[]>("/memos");
}

export function getMemo(memoId: number) {
  return requestJson<Memo>(`/memos/${memoId}`);
}

export function createMemo(payload: {
  title: string;
  remind_at: string | null;
}) {
  return requestJson<Memo>("/memos", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export function updateMemo(
  memoId: number,
  payload: Partial<Pick<Memo, "title" | "done" | "remind_at">>,
) {
  return requestJson<Memo>(`/memos/${memoId}`, {
    method: "PATCH",
    body: JSON.stringify(payload),
  });
}

export function updateMemoDone(memoId: number, done: boolean) {
  return requestJson<Memo>(`/memos/${memoId}/done`, {
    method: "PATCH",
    body: JSON.stringify({ done }),
  });
}

export function deleteMemo(memoId: number) {
  return requestJson<{ message: string }>(`/memos/${memoId}`, {
    method: "DELETE",
  });
}

export function listDueMemos() {
  return requestJson<Memo[]>("/memos/due");
}

export function markMemoNotified(memoId: number) {
  return requestJson<{ message: string }>(`/memos/${memoId}/notified`, {
    method: "PATCH",
  });
}
