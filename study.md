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