import threading
import time
from queue import Queue

class CustomThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            # 要执行的话就需要去队列里面取了
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()

def moyu():
    print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    time.sleep(3)
    print(" 结束摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def queue_pool():
    # 我们创建一个长度为 5 的队列
    queue = Queue(5)
    # 接着根据队列的长度创建了线程
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        # 每个线程都让它们处于守护状态
        t.setDaemon(True)
        t.start()

    for i in range(20):
        # 用 put 方法把我们想做的事情往队列里面塞
        queue.put(moyu)
    queue.join()

if __name__ == '__main__':
    queue_pool()