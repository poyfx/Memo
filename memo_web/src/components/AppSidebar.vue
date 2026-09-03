<script setup lang="ts">
const links = [
  { to: "/memos", label: "备忘录" },
  { to: "/editor", label: "编辑器" },
  { to: "/settings", label: "设置" },
  { to: "/about", label: "关于" },
];
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <h1 class="brand__title">Memo</h1>
      <p class="brand__desc">Tauri + Vue 3 + FastAPI</p>
    </div>

    <nav class="nav">
      <RouterLink
        v-for="link in links"
        :key="link.to"
        :to="link.to"
        class="nav__link"
      >
        <span>{{ link.label }}</span>
        <span>›</span>
      </RouterLink>
    </nav>

    <div class="sidebar__footer">
      <p>桌面备忘录应用</p>
      <p>FastAPI / SQLite / Tauri</p>
    </div>
  </aside>
</template>
