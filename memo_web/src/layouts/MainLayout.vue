<script setup lang="ts">
import AppSidebar from "../components/AppSidebar.vue";
import AppTopbar from "../components/AppTopbar.vue";
import { useReminderPolling } from "../composables/useReminderPolling.ts";

useReminderPolling();
</script>

<template>
  <div class="app-shell">
    <AppSidebar />
    <div class="workspace">
      <AppTopbar />
      <main class="workspace__main">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 280px 1fr;
  background:
    radial-gradient(circle at top, #372a29 0%, #14110f 58%),
    #14110f;
  color: var(--text-main);
}

.workspace {
  min-width: 0;
  display: grid;
  grid-template-rows: auto 1fr;
}

.workspace__main {
  min-width: 0;
  padding: 28px;
  overflow: auto;
}

@media (max-width: 960px) {
  .app-shell {
    grid-template-columns: 1fr;
  }
}
</style>
