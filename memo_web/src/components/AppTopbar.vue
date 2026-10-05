<template>
  <header class="topbar">
    <div>
      <p class="topbar__title">企业项目骨架</p>
      <p class="topbar__subtitle">路由、页面、组件、状态、API 分层</p>
    </div>

    <div class="topbar__actions">
      <el-tag effect="plain">Tauri Desktop</el-tag>
      <el-button plain>同步</el-button>
    </div>
  </header>
</template>

<style scoped>
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 18px 28px;
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

</style>
