# encoding = utf-8
import threading
import time
from concurrent.futures import ThreadPoolExecutor


#
# # 创建一个线程子类
# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程：" + self.name)
#         moyu_time(self.name, self.counter, 10)
#         print("退出线程：" + self.name)
#
#
# def moyu_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s 开始摸鱼 %s" % (threadName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         counter -= 1
#
#
# # 创建新线程
# # 小帅b找了两个人来摸鱼
# # 让小明摸一次鱼休息1秒钟
# # 让小红摸一次鱼休息2秒钟
# thread1 = MyThread(1, "小明", 1)
# thread2 = MyThread(2, "小红", 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# # 等待至线程中止
# thread1.join()
# thread2.join()
# print("退出主线程")


# 仿写
# 创建子线程类
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print("开始线程：" + self.name)
        # 调用摸鱼方法，每人摸鱼10次，休息时间不同
        moyu(self.name, self.counter, 10)
        # 调用摸鱼方法，每人休息时间相同，次数不同
        # moyu(self.name, 1, self.counter)
        print("结束线程：" + self.name)


# 摸鱼方法
def moyu(name, delay, counter):
    while counter:
        time.sleep(delay)
        print("{}开始摸鱼{}".format(name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


# 小明摸鱼一次休息1秒
# 小红摸鱼一次休息2秒
thread1 = MyThread(1, "小明", 1)
thread2 = MyThread(2, "小红", 2)
# 小明摸鱼10次
# 小红摸鱼5次
# thread1 = MyThread(1, "小明", 10)
# thread2 = MyThread(1, "小红", 5)
# 开启线程
print("主线程开始")
thread1.start()
thread2.start()
# 等待线程结束
thread1.join()
thread2.join()
print("主线程结束")
