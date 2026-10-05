import { onMounted, onUnmounted } from "vue";
import { listDueMemos, markMemoNotified } from "../api/memo";
import { notifyDueMemos } from "../services/desktopNotification";
import { useMemoStore } from "../stores/memo";

const POLLING_INTERVAL_MS = 30_000;

 let timerId: number | undefined;
    let checking  = false;

export function useReminderPolling() {
    const memoStore = useMemoStore();


   

    async function checkDueMemos() {
        if(checking ) return;
        checking  = true;
        try{
            const dueMemos = await listDueMemos();
            if(dueMemos.length === 0) return;

            // console.log("到期备忘录:", dueMemos);
            // await Promise.allSettled(
            //     dueMemos.map((memo) => {
            //         markMemoNotified(memo.id);
            //     })
            // )
            const notified = await notifyDueMemos(dueMemos);
            if(!notified)return;

            await Promise.allSettled(
                dueMemos.map((memo)=> markMemoNotified(memo.id))
            )
            await memoStore.refreshMemos();
        }catch (error) {
            console.error("检查到期备忘录时出错:", error);
        } finally {
            checking  = false;
        }
    }

    onMounted(()=>{
        void checkDueMemos()
        timerId = window.setInterval(()=>{
            void checkDueMemos()
        },POLLING_INTERVAL_MS)
    })
    onUnmounted(()=>{
        if(timerId !== undefined){
            window.clearInterval(timerId)
        }
    })
}