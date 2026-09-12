<script setup lang="ts">
import { onBeforeUnmount, onMounted } from "vue";
import heroImg from "../assets/Square89x89Logo.png";
import { invoke } from "@tauri-apps/api/core";
import { getCurrentWindow } from "@tauri-apps/api/window";



let startX = 0;
let startY = 0;
let isMouseDown = false;
let hasDragged = false;

function handleMouseDown(event: MouseEvent) {
  if (event.button !== 0) {
    return;
  }

  isMouseDown = true;
  hasDragged = false;
  startX = event.screenX;
  startY = event.screenY;
}

async function handleMouseMove(event: MouseEvent) {
  if (!isMouseDown || event.buttons !== 1) {
    return;
  }

  const moveX = Math.abs(event.screenX - startX);
  const moveY = Math.abs(event.screenY - startY);

  if (hasDragged || (moveX < 4 && moveY < 4)) {
    return;
  }

  hasDragged = true;
  await getCurrentWindow().startDragging();
}

async function handleMouseUp() {
  isMouseDown = false;

  if (hasDragged) {
    return;
  }

  await invoke("open_main_window");
}
onMounted(() => {
  document.body.classList.add("ball-page");
});

onBeforeUnmount(() => {
  document.body.classList.remove("ball-page");
});
</script>
<template>
 <div
  class="ball-root"
  @mousedown="handleMouseDown"
  @mousemove="handleMouseMove"
  @mouseup="handleMouseUp"
>
  <div class="ball" :style="{ backgroundImage: `url(${heroImg})` }"></div>
</div>
</template>
<style scoped>
:global(body.ball-page) {
  margin: 0;
  overflow: hidden;
  background: transparent !important;
}

:global(body.ball-page #app) {
  width: 56px;
  height: 56px;
  overflow: hidden;
  background: transparent !important;
}
.ball-root {
  width: 56px;
  height: 56px;
  overflow: hidden;
  background: transparent;
  cursor: pointer;
}
.ball-root,
.ball {
  width: 100%;
  height: 100%;
}

.ball-root {
  width: 56px;
  height: 56px;
  overflow: hidden;
}

.ball {
  border-radius: 50%;
  background-color: transparent;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
