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
        <span class="nav__label">{{ link.label }}</span>
        <span class="nav__arrow">›</span>
      </RouterLink>
    </nav>

    <div class="sidebar__footer">
      <p>桌面备忘录应用</p>
      <p>FastAPI / SQLite / Tauri</p>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  padding: 24px 18px;
  background: rgba(12, 10, 9, 0.72);
  border-right: 1px solid var(--border);
  backdrop-filter: blur(18px);
}

.brand {
  margin-bottom: 28px;
}

.brand__title {
  margin: 0;
  font-size: 28px;
}

.brand__desc {
  margin: 8px 0 0;
  color: var(--text-subtle);
  font-size: 14px;
}

.nav {
  display: grid;
  gap: 4px;
}

.nav__link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 11px 12px;
  border-radius: 8px;
  color: var(--text-subtle);
  background: transparent;
  transition: background 0.2s ease, color 0.2s ease;
}

.nav__link:hover,
.nav__link.router-link-active {
  color: var(--text-main);
  background: rgba(240, 179, 106, 0.12);
}

.nav__label {
  font-size: 14px;
}

.nav__arrow {
  color: rgba(244, 239, 232, 0.35);
}

.sidebar__footer {
  margin-top: 28px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
  color: var(--text-subtle);
  font-size: 13px;
}

@media (max-width: 960px) {
  .sidebar {
    border-right: 0;
    border-bottom: 1px solid var(--border);
  }
}
</style>
