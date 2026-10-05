import {isPermissionGranted,requestPermission,sendNotification} from "@tauri-apps/plugin-notification"
import type {Memo} from "../types/memo"

let permissionRequested = false;

function buildNotificationTitle(memos:Memo[]){
    if(memos.length == 1)return memos[0].title;
    return `有${memos.length}条备忘录到期`
}

function buildNotificationBody(memos:Memo[]){
    const lines = memos.slice(0,3).map((memo,index)=>`${index+1}.${memo.title}`)
        if(memos.length>3) lines.push(`等 ${memos.length}条`)
        return lines.join('\n')
}

async function ensureNotificationPermission() {
  let granted = await isPermissionGranted();

  if (granted) {
    return true;
  }

  if (permissionRequested) {
    return false;
  }

  permissionRequested = true;
  granted = (await requestPermission()) === "granted";

  return granted;
}

export async function  notifyDueMemos(memos:Memo[]) {
    if(memos.length === 0) return false;
    const granted = await ensureNotificationPermission();
    if(!granted) return false;
    sendNotification({
        title: buildNotificationTitle(memos),
        body: buildNotificationBody(memos)
    })
    return true
}