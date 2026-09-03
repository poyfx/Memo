import { onMounted, onUnmounted } from "vue";
import { listDueMemos, markMemoNotified } from "../api/memo";
import { notifyDueMemos } from "../services/desktopNotification";


const POLLING_INTERVAL_MS = 30_000;

export function useReminderPolling() {
    let timerId: number | undefined;
    let chhecking = false;

    async function checkDUeMemos() {
        if(chhecking) return;
        chhecking = true;
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

        }catch (error) {
            console.error("检查到期备忘录时出错:", error);
        } finally {
            chhecking = false;
        }
    }

    onMounted(()=>{
        void checkDUeMemos()
        timerId = window.setInterval(()=>{
            void checkDUeMemos()
        },POLLING_INTERVAL_MS)
    })
    onUnmounted(()=>{
        if(timerId !== undefined){
            window.clearInterval(timerId)
        }
    })
}