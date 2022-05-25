# coding=gbk
from pywinauto.application import Application

# 1.����
# start()���ڻ�û����������������timeoutΪ��ʱ��������ѡ������������������ʱ��ϳ���ѡtimeout��Ĭ�ϳ�ʱʱ��Ϊ5s��
# �﷨��start(self, cmd_line, timeout=app_start_timeout)
# app = Application(backend="win32").start("notepad.exe")

# 2.����
# connect()���������Ѿ������ĳ�������һ���Ѿ����еĳ��������¼��ַ�����
# a)process������id
app = Application().connect(process=13624)
print(app)

# b)handle��Ӧ�ó���Ĵ��ھ��
app = Application().connect(handle=0x130A7E)
print(app)

# c)path�����̵�ִ��·����GetModuleFileNameEx ģ�����ҽ��̵�ÿһ��·���������Ǵ����·��ȥ���Ƚϣ�
# app = Application().connect(path=��D:\Office14\EXCEL.exe��)

# d)������ϣ����ݸ�pywinauto.findwindows.find_elements()���������
app = Application().connect(title_re="test.txt - ���±�", class_name="Notepad")
print(app)

# �ġ� ���ڡ��Ի��򼰿ؼ�Ԫ�ض�λ��ʽ
# 1.window��dialog��λ��ʽ
# 1)����title��λ
# a)ʹ��title��λ��ʽ��д��
# Untitled_notepad = u"test.txt - ���±�"
# app.Untitled_notepad.draw_outline(colour="red")
# ����
app["test.txt - ���±�"].draw_outline(colour="red")
print(app)

# 2)top_window()��λ
# app.top_window() #�˷����ɷ���Ӧ���������㴰�ڣ��Ǵ��ڣ����Ǵ��ڵ����ĶԻ���
# ע���˷���Ŀǰû�о������ԣ����᷵��Ӧ�ó���Ķ������ڣ������ܲ���Z-Order�еĶ������ڡ�

# 3)�ؼ��ִ���
# �����Ϸ����������㶨λԪ�ص����󣬿�ʹ�������б��еĲ������ζ�λԪ�أ������������ʹ�á�
# ʾ����
app.window(class_name="Notepad").draw_outline(colour="red")
print(app)

# 2�� control��λ��ʽ
# ����title��λ��ͬwindow��dialog�е�title��λ��
app["test.txt - ���±�"]
print(app)
# ��
# app.dlg.control