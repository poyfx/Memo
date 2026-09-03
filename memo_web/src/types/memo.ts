export interface Memo {
  id: number;
  title: string;
  done: boolean;
  remind_at: string | null;
  notified: boolean;
}
