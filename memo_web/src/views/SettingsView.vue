<template>
  <section class="page">
    <div class="panel">
      <h2 class="panel__title">设置</h2>
      <p class="panel__desc">后续放提醒开关、托盘行为、启动项等桌面配置。</p>
    </div>

    <div class="grid grid--2">
      <div class="panel">
        <h3 class="panel__title">提醒</h3>
        <p class="panel__desc">通知方式、重复提醒、静默时间。</p>
      </div>
      <div class="panel">
        <h3 class="panel__title">桌面</h3>
        <p class="panel__desc">托盘、悬浮球、开机启动。</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.page {
  display: grid;
  gap: 20px;
}

.grid {
  display: grid;
  gap: 16px;
}

.grid--2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.panel {
  padding: 20px;
  border-radius: 20px;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}

.panel__title {
  margin: 0 0 10px;
  font-size: 18px;
}

.panel__desc {
  margin: 0;
  color: var(--text-subtle);
}

@media (max-width: 960px) {
  .grid--2 {
    grid-template-columns: 1fr;
  }
}
</style>
