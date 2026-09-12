<template>
  <section class="page">
    <div class="panel">
      <h2 class="panel__title">编辑器</h2>
      <p class="panel__desc">后续放单条备忘录编辑、右侧预览、提醒时间修改。</p>
    </div>

    <div class="panel">
      <h3 class="panel__title">编辑草稿</h3>
      <p class="panel__desc">这里会接入单条编辑表单和详情面板。</p>
    </div>
  </section>
</template>

<style scoped>
.page {
  display: grid;
  gap: 20px;
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
</style>
