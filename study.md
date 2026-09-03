# Python / FastAPI 学习笔记

日期：2026-09-02

## 当前目标
- 学习 Python 基础
- 继续推进 FastAPI
- 最终做一个 Windows 桌面备忘录应用

## 已学到的内容
- Python 函数、返回值、条件、循环、导入
- 文件读写、JSON、argparse、异常处理
- FastAPI 最小项目
- GET / POST / PUT / PATCH / DELETE
- BaseModel、response_model、HTTPException
- SQLite 增删改查
- `remind_at` 和 `notified`
- `/memos/due`
- Tauri 项目结构
- Vue 3 前端骨架

## 当前后端状态
- 后端主线已经跑通到“提醒系统基础”
- 接下来要做前后端联调

## 当前前端状态
- `memo_web` 已切到 Vue 3
- 已有 Router、Pinia、layouts、views、components、api、stores、types
- 现在可以开始接 FastAPI

## 下一步
- 先接 `GET /memos`
- 再接 `POST /memos`
- 然后接 `PATCH /memos/{id}` 和 `PATCH /memos/{id}/done`
- 最后做提醒、托盘、悬浮球
