import time
from multiprocessing import Process

def f(name):
    print("开始线程：" + name)
    time.sleep(3)
    print("结束线程：" + name)

if __name__ == '__main__':
    p1 = Process(target=f, args=('小明',))
    p2 = Process(target=f, args=('小红',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()