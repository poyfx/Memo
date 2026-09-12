<template>
  <div class="empty-state">
    <h3 class="panel__title">这里还没有备忘录</h3>
    <p class="panel__desc">先添加一条，后面再接 FastAPI 数据。</p>
  </div>
</template>

<style scoped>
.empty-state {
  padding: 28px;
  text-align: center;
  color: var(--text-subtle);
}

.panel__title {
  margin: 0 0 10px;
  font-size: 18px;
  color: var(--text-main);
}

.panel__desc {
  margin: 0;
  color: var(--text-subtle);
}
</style>
