数据模型第一版
- id
- title
- content
- remind_at
- is_done
- created_at
- updated_at
第一阶段学习目标
- 跑通 FastAPI 最小项目
- 学会 GET / POST
- 学会打开 /docs
- 先做内存版备忘录接口
- 后续再接 SQLite
14 天大致路线
1. FastAPI 最小项目
2. GET /memos
3. POST /memos
4. DELETE /memos/{id}
5. PUT /memos/{id}
6. 用内存列表跑通 CRUD
7. 接入 SQLite
8. 整理后端结构
9. 起 Tauri 桌面壳
10. 做备忘录列表页
11. 接口联调
12. 加托盘
13. 加悬浮球
14. 加提醒和测试
每天学习安排
- 每天 2 到 3 小时
- 40 分钟学知识点
- 80 分钟敲代码
- 20 分钟整理笔记









这是开始新窗口文案
今天是 2026-08-30，请接着我当前的学习进度继续，不要从头开始讲。

我的情况：
- 我有前端开发经验
- 我正在补 Python
- 我已经做过一个 Python CLI 待办事项小项目
- 我现在准备直接学习 FastAPI
- 我的目标是做一个 Windows 桌面备忘录应用

产品目标：
- 新增备忘录
- 删除备忘录
- 编辑备忘录
- 标记完成
- 到点提醒
- 悬浮球
- 系统托盘

技术路线：
- FastAPI
- SQLite
- Tauri

当前工作目录：
- E:\python\first-project

当前文件：
- 学习笔记：study.md
- 项目计划：fastapi_memo_plan.md
- FastAPI 项目准备放在：memo_backend/main.py

学习方式：
- 每天学习 2 到 3 小时
- 少讲空泛理论，多按项目一步一步带
- 需要代码时，直接给我可写入文件的版本
- 如果我说“继续”，就按当前路线继续

当前进度：
- Python CLI 项目已经学过函数、返回值、文件读写、json、argparse、命令行模式、异常处理
- 现在准备正式开始 FastAPI
- 下一步要做的是：创建 memo_backend/main.py，写最小可运行的 FastAPI 程序，跑通 / 和 /docs，然后继续做 GET /memos 和 POST /memos

请现在直接从这一步开始带我。