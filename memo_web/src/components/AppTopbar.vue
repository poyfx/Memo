<template>
  <header class="topbar">
    <div>
      <p class="topbar__title">企业项目骨架</p>
      <p class="topbar__subtitle">路由、页面、组件、状态、API 分层</p>
    </div>

    <div class="topbar__actions">
      <span class="badge">Tauri Desktop</span>
      <button class="button button--ghost" type="button">同步</button>
    </div>
  </header>
</template>

<style scoped>
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 22px 28px;
  border-bottom: 1px solid var(--border);
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(18px);
}

.topbar__title {
  margin: 0;
  font-size: 22px;
}

.topbar__subtitle {
  margin: 4px 0 0;
  color: var(--text-subtle);
  font-size: 13px;
}

.topbar__actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.badge {
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(240, 179, 106, 0.12);
  color: var(--brand-strong);
  font-size: 13px;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 40px;
  padding: 0 14px;
  border-radius: 12px;
  background: var(--brand);
  color: #24170f;
  font-weight: 600;
  border: 0;
}

.button--ghost {
  background: rgba(255, 255, 255, 0.07);
  color: var(--text-main);
}
</style>
