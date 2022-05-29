# coding=gbk
from pywinauto.application import Application

# 1.启动
# start()用于还没有启动软件的情况。timeout为超时参数（可选），若软件启动所需的时间较长可选timeout，默认超时时间为5s。
# 语法：start(self, cmd_line, timeout=app_start_timeout)
# app = Application(backend="win32").start("notepad.exe")

# 2.连接
# connect()用于连接已经启动的程序。连接一个已经运行的程序有以下几种方法：
# a)process：进程id
app = Application().connect(process=13624)
print(app)

# b)handle：应用程序的窗口句柄
app = Application().connect(handle=0x130A7E)
print(app)

# c)path：进程的执行路径（GetModuleFileNameEx 模块会查找进程的每一个路径并与我们传入的路径去做比较）
# app = Application().connect(path=“D:\Office14\EXCEL.exe”)

# d)参数组合（传递给pywinauto.findwindows.find_elements()这个函数）
app = Application().connect(title_re="test.txt - 记事本", class_name="Notepad")
print(app)

# 四、 窗口、对话框及控件元素定位方式
# 1.window，dialog定位方式
# 1)基于title定位
# a)使用title定位方式的写法
# Untitled_notepad = u"test.txt - 记事本"
# app.Untitled_notepad.draw_outline(colour="red")
# 或者
app["test.txt - 记事本"].draw_outline(colour="red")
print(app)

# 2)top_window()定位
# app.top_window() #此方法可返回应用软件的最顶层窗口（是窗口，不是窗口弹出的对话框）
# 注：此方法目前没有经过测试，它会返回应用程序的顶级窗口，但可能不是Z-Order中的顶级窗口。

# 3)关键字传参
# 若以上方法不能满足定位元素的需求，可使用以下列表中的参数传参定位元素，参数可以组合使用。
# 示例：
app.window(class_name="Notepad").draw_outline(colour="red")
print(app)

# 2． control定位方式
# 基于title定位（同window，dialog中的title定位）
app["test.txt - 记事本"]
print(app)
# 或
# app.dlg.control