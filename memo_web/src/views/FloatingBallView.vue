<script setup lang="ts">
import { ref } from "vue";

import { onBeforeUnmount, onMounted } from "vue";
import { invoke } from "@tauri-apps/api/core";
import { getCurrentWindow ,LogicalSize,PhysicalPosition,currentMonitor } from "@tauri-apps/api/window";

import heroImg from "../assets/Square89x89Logo.png";


let startX = 0;
let startY = 0;
let isMouseDown = false;
let hasDragged = false;
// 吸附后 根据位置显示菜单
let beforeMenuX = 0;
let beforeMenuY = 0;
let isMenuWindowOpen = false;

const BALL_SIZE = 56;
const MENU_WINDOW_WIDTH = 148;
const MENU_WINDOW_HEIGHT = 112;
const MENU_LEFT_OFFSET = MENU_WINDOW_WIDTH - BALL_SIZE; // 92

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
  
  if (menuVisible.value) {
    await resetBallWindow();
  return;
    }

    await ballWindow.startDragging();
  snapBallToEdgeSoon()
}
// 短时间记录 用户拖拽位置
function snapBallToEdgeSoon() {
  const delays = [800, 1400];

  delays.forEach((delay) => {
    setTimeout(() => {
      void snapBallToEdge();
    }, delay);
  });
}
async function handleMouseUp(event: MouseEvent) {
  if (event.button !== 0) {
    return;
  }

  isMouseDown = false;

  if (hasDragged) {
    return;
  }

  if (menuVisible.value) {
    await resetBallWindow();
  return;
  }

  await invoke("open_main_window");
}


//悬浮球增加菜单
const ballWindow = getCurrentWindow();

const menuVisible = ref(false);

async function openMenu(event: MouseEvent) {
  event.preventDefault();

  isMouseDown = false;
  hasDragged = false;

  const position = await ballWindow.outerPosition();

  beforeMenuX = position.x;
  beforeMenuY = position.y;
  isMenuWindowOpen = true;

  menuVisible.value = true;
  document.documentElement.classList.add("ball-menu-open");
  document.body.classList.add("ball-menu-open");

  await ballWindow.setPosition(
    new PhysicalPosition(position.x - MENU_LEFT_OFFSET, position.y),
  );
  await ballWindow.setSize(
    new LogicalSize(MENU_WINDOW_WIDTH, MENU_WINDOW_HEIGHT),
  );
}


async function handleOpenMainWindow() {
   await resetBallWindow();
  await invoke("open_main_window");
}

async function handleQuitApp() {
  await invoke("quit_app");
}
//记录悬浮球位置
const BALL_POSITION_KEY = "memo-floating-ball-position";

async function saveBallPosition() {
  if (menuVisible.value || isMenuWindowOpen) {
    return;
  }

  const position = await ballWindow.outerPosition();

  localStorage.setItem(
    BALL_POSITION_KEY,
    JSON.stringify({
      x: position.x,
      y: position.y,
    }),
  );
}

async function restoreBallPosition() {
  const raw = localStorage.getItem(BALL_POSITION_KEY);

  if (!raw) {
    return;
  }

  const position = JSON.parse(raw) as { x: number; y: number };
  await ballWindow.setPosition(new PhysicalPosition(position.x, position.y));
}
//吸附
async function snapBallToEdge() {
  const monitor = await currentMonitor();

  if (!monitor) {
    await saveBallPosition();
    return;
  }

  const position = await ballWindow.outerPosition();

  const ballSize = 56;
  const edgeGap = 8;

  const screenLeft = monitor.position.x;
  const screenTop = monitor.position.y;
  const screenWidth = monitor.size.width;
  const screenHeight = monitor.size.height;

  const centerX = position.x + ballSize / 2;
  const screenCenterX = screenLeft + screenWidth / 2;

  const targetX =
    centerX < screenCenterX
      ? screenLeft + edgeGap
      : screenLeft + screenWidth - ballSize - edgeGap;

  const minY = screenTop + edgeGap;
  const maxY = screenTop + screenHeight - ballSize - edgeGap;
  const targetY = Math.min(Math.max(position.y, minY), maxY);

  await ballWindow.setPosition(new PhysicalPosition(targetX, targetY));
  await saveBallPosition();
}

async function resetBallWindow() {
  menuVisible.value = false;

  document.documentElement.classList.remove("ball-menu-open");
  document.body.classList.remove("ball-menu-open");

  if (isMenuWindowOpen) {
    await ballWindow.setPosition(new PhysicalPosition(beforeMenuX, beforeMenuY));
  }

  await ballWindow.setSize(new LogicalSize(BALL_SIZE, BALL_SIZE));

  isMenuWindowOpen = false;
}
function handleKeydown(event: KeyboardEvent) {
  if (event.key !== "Escape") {
    return;
  }

  if (!menuVisible.value) {
    return;
  }

  void resetBallWindow();
}

onMounted(async () => {
  document.documentElement.classList.add("ball-page");
  document.body.classList.add("ball-page");
  window.addEventListener("keydown", handleKeydown);
  await restoreBallPosition();
});

onBeforeUnmount(() => {
  document.documentElement.classList.remove("ball-page", "ball-menu-open");
  document.body.classList.remove("ball-page", "ball-menu-open");
});
</script>
<template>
 <div
  class="ball-root"
 :class="[
  { 'menu-open': menuVisible },
]"
  @contextmenu="openMenu"
  @mousedown="handleMouseDown"
  @mousemove="handleMouseMove"
  @mouseup="handleMouseUp"
>
  <div class="ball" :style="{ backgroundImage: `url(${heroImg})` }"></div>

  <div
  v-if="menuVisible"
  class="ball-menu"
  @mousedown.stop
  @mouseup.stop
  @click.stop
>
  <button @click="handleOpenMainWindow">打开</button>
  <button @click="handleQuitApp">退出</button>
</div>
</div>
</template>
<style scoped>
.ball-root {
  position: relative;
  width: 56px;
  height: 56px;
  overflow: hidden;
  background: transparent;
  cursor: pointer;
}

.ball-root.menu-open {
  width: 148px;
  height: 112px;
  overflow: visible;
}

.ball {
  position: absolute;
  left: 0;
  top: 0;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background-color: transparent;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.ball-root.menu-open .ball {
  left: 92px;
}

.ball-menu {
  position: absolute;
  left: 8px;
  top: 8px;
  width: 76px;
  padding: 6px;
  border-radius: 8px;
  background: rgba(32, 32, 32, 0.96);
}
</style>
