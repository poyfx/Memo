import { createRouter, createWebHashHistory } from "vue-router";
import MainLayout from "../layouts/MainLayout.vue";
import MemoListView from "../views/MemoListView.vue";
import MemoEditorView from "../views/MemoEditorView.vue";
import SettingsView from "../views/SettingsView.vue";
import AboutView from "../views/AboutView.vue";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/",
      component: MainLayout,
      children: [
        {
          path: "",
          redirect: "/memos",
        },
        {
          path: "memos",
          name: "memos",
          component: MemoListView,
          meta: { title: "备忘录" },
        },
        {
          path: "editor",
          name: "editor",
          component: MemoEditorView,
          meta: { title: "编辑器" },
        },
        {
          path: "settings",
          name: "settings",
          component: SettingsView,
          meta: { title: "设置" },
        },
        {
          path: "about",
          name: "about",
          component: AboutView,
          meta: { title: "关于" },
        },
      ],
    },
  ],
});

router.afterEach((to) => {
  const pageTitle = to.meta.title ? `${to.meta.title} · Memo` : "Memo";
  document.title = pageTitle;
});

export default router;
