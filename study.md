1、python -m venv .venv
2、激活虚拟环境：.\.venv\Scripts\activate
3、安装依赖：pip install 包名，比如 pip install requests
4、切换解释器：在 VS Code 里选 .\.venv\Scripts\python.exe
5、pip freeze > requirements.txt （导出依赖包命令）
6、pip install -r requirements.txt 批量安装依赖
退出虚拟环境：deactivate



# Python 项目笔记

## 1. 关键词 / 语法
- def：定义函数
- return：返回结果
- if / elif / else：条件判断
- for：循环
- import：导入模块

## 2. 字符串常用方法
- strip()：去掉首尾空格
- lower()：转小写
- join()：把列表拼成字符串
- split()：把字符串拆成列表
- isdigit()：判断是不是数字字符串

## 3. 列表 / 字典常用方法
- append()：列表末尾添加
- pop(index)：删除并返回指定元素
- enumerate()：循环时同时拿到编号和内容
- get()：安全获取字典值

## 4. 当前项目常用标准库
- argparse.ArgumentParser()：创建命令行解析器
- add_subparsers()：创建子命令
- add_parser()：定义 add/list/done 这些命令
- add_argument()：定义命令参数
- parse_args()：解析命令行参数
- print_help()：打印帮助信息

- sys.argv：获取命令行参数
- raise SystemExit(...)：返回命令行退出码

- json.load()：读取 json
- json.dump()：写入 json

- Path(__file__).parent：当前文件所在目录
- datetime.now().strftime(...)：格式化当前时间

## 命令行参数
- argparse.ArgumentParser()：创建解析器
- add_subparsers()：创建子命令
- add_parser()：创建 add/list/done 等命令
- add_argument()：给命令加参数
- parse_args()：解析参数
- print_help()：打印帮助说明

## 输入处理
- strip()：去掉首尾空格
- join()：把列表拼成字符串
- isdigit()：判断是不是数字
- isinstance(x, list)：判断类型

## 列表和字典
- append()：添加元素
- pop(index)：删除元素
- enumerate()：拿到序号和内容
- get()：安全获取字典字段

## 返回值设计
- return True：执行成功
- return False：执行失败
- return None：通常表示没找到或无结果


# Python / FastAPI 学习笔记

日期：2026-08-30

## 当前目标
- 学习 Python 基础
- 直接进入 FastAPI
- 最终做一个 Windows 桌面备忘录应用

## Python 基础关键词
- def：定义函数
- return：返回结果
- if / elif / else：条件判断
- for：循环
- import：导入模块
- try / except：异常处理

## 字符串常用方法
- strip()：去掉首尾空格
- lower()：转小写
- join()：把列表拼成字符串
- split()：把字符串拆成列表
- isdigit()：判断是否为数字字符串

## 列表和字典常用方法
- append()：向列表末尾添加元素
- pop(index)：删除并返回指定元素
- enumerate()：循环时同时拿到索引和内容
- get()：安全获取字典字段值

## 当前项目中用到的标准库
- argparse.ArgumentParser()：创建命令行解析器
- add_subparsers()：创建子命令
- add_parser()：创建 add/list/done 等命令
- add_argument()：给命令添加参数
- parse_args()：解析命令行参数
- print_help()：打印帮助信息

- sys.argv：获取命令行参数
- raise SystemExit(...)：返回命令行退出码

- json.load()：读取 JSON 文件
- json.dump()：写入 JSON 文件

- Path(__file__).parent：获取当前文件所在目录
- datetime.now().strftime(...)：格式化当前时间

## FastAPI 预习关键词
- FastAPI()：创建应用
- @app.get()：定义 GET 接口
- @app.post()：定义 POST 接口
- BaseModel：定义请求数据结构
- uvicorn：运行 FastAPI 服务
- /docs：自动生成接口文档

## 当前项目里学到的编程思想
- 重复逻辑要抽函数
- 输入处理和业务处理要分开
- 菜单模式和命令行模式可以共用一套业务逻辑
- 先让程序能跑，再慢慢优化结构
- 不需要死记 API，要记“它在项目里干什么”

## 我现在最需要记住的 10 个点
- def
- return
- if
- for
- append
- pop
- strip
- join
- isdigit
- json.dump

## 今日提醒
- 不追求一次记住全部
- 先会用，再慢慢记
- 每学完一个知识点，都结合项目写一个小例子


## 学习阶段记录

日期：2026-09-01

### 已学到的内容
- FastAPI 最小可运行程序
- `@app.get()` / `@app.post()` / `@app.put()` / `@app.patch()` / `@app.delete()`
- `BaseModel` 请求体校验
- `response_model` 返回值约束
- `HTTPException` 返回 404
- SQLite 的增删改查
- `memos.db` 表结构设计
- `remind_at` 提醒时间字段
- `notified` 已提醒字段
- `/memos/due` 到点提醒查询
- `GET /memos`、`POST /memos`、`PATCH /memos/{memo_id}`、`PATCH /memos/{memo_id}/done`
- 错误判断：`422` 多半是请求体，`500` 多半是代码，`404` 多半是路径或数据

### 关键理解
- FastAPI 负责接口和数据校验
- SQLite 负责数据持久化
- `db.py` 负责数据库操作
- `main.py` 负责路由和 HTTP 错误
- `schemas.py` 负责请求体和返回体结构
- `remind_at` 用来表示提醒时间
- `notified` 用来避免重复提醒
- `done` 表示任务是否完成

### 目前进度
- 后端主线已经跑通到“提醒系统基础”
- 前端和 Tauri 还没有正式开始
- 目前还没有学 Tauri 项目结构

### 下一步准备学的内容
- Tauri 项目结构
- 前端页面最小结构
- 前端如何调用 FastAPI
- 系统通知、系统托盘、悬浮球
