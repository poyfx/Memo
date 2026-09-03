# FastAPI 桌面备忘录项目计划

日期：2026-09-02

## 项目目标
做一个 Windows 桌面备忘录应用。

## 第一版核心功能
- 新增备忘录
- 删除备忘录
- 编辑备忘录
- 标记完成
- 到点提醒
- 悬浮球
- 系统托盘

## 技术方案
- 后端：FastAPI
- 数据库：SQLite
- 桌面端：Tauri
- 前端：Vue 3

## 当前状态
- FastAPI 后端已跑通到提醒系统基础
- Vue 3 前端企业骨架已搭好
- Tauri 项目结构已学完
- `tauri dev` 已可启动

## 已完成的后端内容
- `GET /`
- `GET /memos`
- `GET /memos/{memo_id}`
- `POST /memos`
- `PUT /memos/{memo_id}`
- `PATCH /memos/{memo_id}`
- `PATCH /memos/{memo_id}/done`
- `PATCH /memos/{memo_id}/notified`
- `GET /memos/due`
- SQLite CRUD
- `remind_at`
- `notified`

## 已完成的前端内容
- Vite 初始化
- Tauri 初始化
- Vue 3 迁移
- Vue Router
- Pinia
- 路由分层
- 布局分层
- 页面分层
- 组件分层
- API 分层
- 状态分层

## 下一步
- 前端联调 FastAPI
- 先接 `GET /memos`
- 再接 `POST /memos`
- 然后接 `PATCH /memos/{id}` 和 `PATCH /memos/{id}/done`
- 最后做提醒、托盘、悬浮球
