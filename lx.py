# coding=gbk
import os

os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
from pywinauto.application import Application

# ��������
app = Application().connect(process=44936)
# ��ȡ���±�����
dlg = app.window(class_name="Notepad")
# �̵��Ƿ�Ϊdialog
print(dlg.is_dialog)
# ���ؼ��������
dlg.draw_outline(colour="red")
# ��ӡ��ǰ�������еĿؼ�������
dlg.print_control_identifiers(depth=None, filename=None)
# �����ַ�
# dlg.type_keys("file_name_path")
# ʹ�ÿ�ݼ�����ѡ��
dlg.type_keys('^F')

