<script setup lang="ts">
import AppSidebar from "../components/AppSidebar.vue";
import AppTopbar from "../components/AppTopbar.vue";
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
