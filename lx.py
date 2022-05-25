# coding=gbk
import os

os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
from pywinauto.application import Application

# 创建连接
app = Application().connect(process=44936)
# 获取记事本窗口
dlg = app.window(class_name="Notepad")
# 盘点是否为dialog
print(dlg.is_dialog)
# 给控件画个红框
dlg.draw_outline(colour="red")
# 打印当前窗口所有的控件和属性
dlg.print_control_identifiers(depth=None, filename=None)
# 输入字符
# dlg.type_keys("file_name_path")
# 使用快捷键进行选择
dlg.type_keys('^F')

