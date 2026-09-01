# print("你好")
# name = input("你叫什么名字")
# print('你好'+name)
# age = int(input('你几岁？'))
# if age >= 18 :
#    print("你是成年人了")
# else:
#    print("你还未成年")

# for i in range(5):
#    print(i)

# i = 0
# while i < 5:
#    print(i)
#    i+=1

# def greet(name):
#    print('你好'+name)

# greet('小米')

# fruits = ['苹果','橘子','橙子']
# print(fruits[0])
# print(len(fruits))

# obj = {'name':"小米","age":18}
# print(obj['name'])
# print(obj["age"])

# def add(a , b):
#     return a + b
# print(add(1,2))

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def say_hallo(self):
#         print('你好：'+ self.name)

# p=Person('小米')
# p.say_hallo()

# class Animal:
#     def speak(self):
#         print('叫')
# class Dog(Animal):
#     def speak(self):
#         print('汪汪')
# d = Dog()
# d.speak()
# import random
# print(random.randint(1,10))
# import mymath
# print(mymath.add(1,2))
# from mytool import math
# print(math.add(1,2))
# try:
#    num = int(input('请输入一个数字'))
#    print(10/num)
# except ValueError:
#    print("不是一个数字")
# except ZeroDivisionError:
#    print("不能输入0")
# finally:
#    print("程序结束")
# with open("a.txt",'w',encoding='utf-8') as f:
#     f.write('hello')
# with open("a.txt","r",encoding='utf-8') as f:
#     print(f.read())

# nums = [1,2,3,4,5]
# sua = [x*x for x in nums]
# print(sua)
# nums = [1,2,3,4,5,6]
# print(list(map(lambda x:x*2,nums)))
# print(list(filter(lambda x: x%2 == 0,nums)))
# point = (1,2)
# print(point[0])
# nums = {1,2,2,3}
# print(nums)
# score = 85
# if score >= 60:
#     print('及格')
# else:
#     print('不及格')
# for i in range(5):
#     if i == 2:
#         break
#     print(i)
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# def greet(name='朋友'):
#     print('你好'+name)

# greet()
# greet('小米')

# def all_add(*numbers):
#     print(sum(numbers))

# all_add(1,2,3,4)
# def show_info(**keyword):
#     print(keyword)
# show_info(name="小米",age=18)

# name = '小明'
# age = 18
# message = f"我叫{name},今年{age}岁"
# print(message)

# fruits = ['苹果','栗子','香蕉']
# for index,fruit in enumerate(fruits):
#     print(index,fruit)
# person={
#     'name':'小米',
#     'age':18
# }
# for key,value in person.items():
#     print(key ,value)

# names = ['小米','小红','小哥']
# ages=[18,16,23]
# for name,age in zip(names,ages):
#     print(name,age)

# nums = [1,3,4,6,2,4,5]
# print(sorted(nums))
# print(sorted(nums,reverse=True))

# student = [
#     {
#         'name':"刚子",
#         "score":60
#     },
#     {
#         'name':"洪雅",
#         "score":80
#     },
#     {
#         'name':"轩子",
#         "score":90
#     }
# ]

# result = sorted(student,key= lambda student:student['score'],reverse=True)
# print(result)

# import os
# print(os.getcwd)

# import sys
# print(sys.version)

from datetime import datetime
from storage import load_tasks, save_tasks
from tasks import (
    create_task,
    mark_done,
    find_tasks,
    update_task_title,
    remove_task,
    get_task_stats,
)
import argparse
import sys

# DATA_FILE = Path(__file__).parent / "tasks.json"

# def save_tasks(tasks):
#     with DATA_FILE.open('w',encoding="utf-8") as file:
#         json.dump(tasks,file,ensure_ascii=False,indent=2)

# def load_tasks():
#     if not DATA_FILE.exists():
#         return
#     with DATA_FILE.open('r',encoding="utf-8") as file:
#         data = json.load(file)
#         return [
#             {
#                 'title':item,'done':False
#             }if isinstance(item,str)else item for item in data
#         ]


def add_task(task):
    title = input("请输入任务内容：").strip()
    handle_add(title, task)
    # if title == "":
    #     print("不能为空")
    #     return
    # list = create_task(title)

    # task.append(list)
    # save_tasks(task)
    # print(f"已添加任务{title}")
    # print(f"当前任务{task}")


def list_task(tasks):
    if not tasks:
        print("暂无任务")
        return False
    for index, task in enumerate(tasks, start=1):
        status = "已完成" if task["done"] else "未完成"
        create_at = task.get("create_at", "未知时间")
        complete_at = task.get("complete_at")

        if complete_at:
            print(f"{index}. [{status}]{task['title']},完成于：{complete_at}")
        else:
            print(f"{index}. [{status}]{task['title']}")
    return True


def detele_tasks(tasks):

    if not list_task(tasks):
        print("暂无任务")
        return

    choice = input("请输入要删除任务的编号：").strip()
    handle_delete(choice, tasks)
    # list_task(tasks)
    # if not tasks:
    #     return
    # choice = input("请输入要删除任务的编号：")
    # if not choice.isdigit():
    #     print("请输入数字编号")
    #     return
    # index = int(choice) - 1
    # removed_task = remove_task(tasks, index)
    # if removed_task is None:
    #     print("任务不存在")
    #     return
    # save_tasks(tasks)
    # print(f"已删除任务：{removed_task['title']}")


def complete_task(tasks):
    list_task(tasks)
    if not tasks:
        return
    choice = input("请输入已完成的任务编号：")
    if not choice.isdigit():
        print("请输入数字编号")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("任务编号不存在")
        return
    # if tasks[index]["done"]:
    #     print('该任务已完成')
    #     return

    # tasks[index]['done'] = True
    # tasks[index]['complete_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    success = mark_done(tasks[index])
    if not success:
        print("这个任务已完成")
        return

    save_tasks(tasks)
    print(f"已完成任务{tasks[index]['title']}")


def show_state(task):
    total, complete, pending = get_task_stats(task)
    print(f"总任务：{total}")
    print(f"已完成：{complete}")
    print(f"未完成；{pending}")


def edit_task(tasks):
    list_task(tasks)
    if not tasks:
        return
    choice = input("请输入修改编号：")
    if not choice.isdigit():
        print("请输入数字编号")
        return
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("任务编号不存在")
        return

    new_title = input("请输入编辑文案").strip()
    if new_title == "":
        print("请输入内容")
        return

    update_task_title(tasks[index], new_title)
    save_tasks(tasks)
    print("修改成功")


def search_tasks(tasks):
    keyword = input("请输入搜索内容").strip()
    if keyword == "":
        print("请输入搜索内容")
        return
    found = False

    for index, task in enumerate(tasks, start=1):
        if keyword.lower() in task["title"].lower():
            status = "已完成" if task["done"] else "未完成"
            print(f"{index}. [{status}]{task['title']}")
            found = True
    if not found:
        print("未找到内容")


def get_task_index(value, tasks):
    if not value or not value.isdigit():
        print("请输入数字编号")
        return None

    index = int(value) - 1

    if index < 0 or index >= len(tasks):
        print("输入编号不存在")
        return None

    return index


def handle_add(value, tasks):
    value = normlize_text(value)
    if not value:
        print("请提供任务内容")
        return False
    task = create_task(value)
    tasks.append(task)
    save_tasks(tasks)
    print(f"已添加任务：{value}")
    return True


def handle_delete(value, tasks):
    index = get_task_index(value, tasks)
    if index is None:
        return False

    removed_task = remove_task(tasks, index)
    save_tasks(tasks)
    print(f'已删除任务：{removed_task["title"]}')
    return True


def handle_done(value, tasks):
    index = get_task_index(value, tasks)
    if index is None:
        return False

    success = mark_done(tasks[index])
    if not success:
        print("这个任务已经完成")
        return False

    save_tasks(tasks)
    print(f"已经完成任务：{tasks[index]['title']}")
    return True


def handle_search(value, tasks):
    value = normlize_text(value)
    if not value:
        print("请输入搜索内容")
        return False

    results = find_tasks(value, tasks)
    if not results:
        print("未找到内容")
        return False
    for index, task in enumerate(results, start=1):
        status = "已完成" if task["done"] else "未完成"
        print(f"{index}. [{status}]{task['title']}")
    return True


def handle_edit(value, extra, tasks):
    value = normlize_text(value)
    index = get_task_index(value, tasks)
    if index is None:
        return False

    if not extra:
        print("请输入编辑文案")
        return False
    new_word = " ".join(extra)
    update_task_title(tasks[index], new_word)
    save_tasks(tasks)
    print("修改成功")
    return True


def normlize_text(text):
    if isinstance(text, list):
        text = " ".join(text)
    return text.strip()


def run_command_mode():
    parser = argparse.ArgumentParser(description="待办事项工具")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="添加任务")
    add_parser.add_argument("title", nargs="+", help="任务内容")

    list_parser = subparsers.add_parser("list", help="查看任务")

    done_parser = subparsers.add_parser("done", help="标记任务为完成")
    done_parser.add_argument("index", help="任务编号")

    delete_parser = subparsers.add_parser("delete", help="删除任务")
    delete_parser.add_argument("index", help="任务编号")

    search_parser = subparsers.add_parser("search", help="搜索任务")
    search_parser.add_argument("keyword", nargs="+")

    edit_parser = subparsers.add_parser("edit", help="编辑任务")
    edit_parser.add_argument("index", help="任务编号")
    edit_parser.add_argument("title", nargs="+", help="新任务内容")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return 1

    tasks = load_tasks()

    commands = {
        "list": lambda: list_task(tasks),
        "add": lambda: handle_add(normlize_text(args.title), tasks),
        "done": lambda: handle_done(args.index, tasks),
        "delete": lambda: handle_delete(args.index, tasks),
        "search": lambda: handle_search(normlize_text(args.keyword), tasks),
        "edit": lambda: handle_edit(args.index, normlize_text(args.title), tasks),
    }

    action = commands.get(args.command)
    if action is None:
        print("无效的命令")
        return 1
    result = action()
    return 0 if result is not False else 1
    # if args.command == "add":
    #     handle_add(" ".join(args.title), tasks)
    # elif args.command == "list":
    #     list_task(tasks)
    # elif args.command == "done":
    #     handle_done(args.index, tasks)
    # elif args.command == "delete":
    #     handle_delete(args.index, tasks)
    # elif args.command == "search":
    #     handle_search(" ".join(args.keyword), tasks)
    # elif args.command == "edit":
    #     handle_edit(args.index, " ".join(args.title), tasks)


def main():
    task = load_tasks()
    while True:
        print("待办事项工具")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 删除任务")
        print("4. 完成任务")
        print("5. 查看统计")
        print("6. 修改任务")
        print("7. 查找内容")
        print("8. 退出")

        choice = input("请选择：")

        if choice == "1":
            add_task(task)
        elif choice == "2":
            list_task(task)
        elif choice == "3":
            detele_tasks(task)
        elif choice == "4":
            complete_task(task)
        elif choice == "5":
            show_state(task)
        elif choice == "6":
            edit_task(task)
        elif choice == "7":
            search_tasks(task)
        elif choice == "8":
            print("程序结束")
            break
        else:
            print("无效选择")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        raise SystemExit(run_command_mode())
    else:
        main()
