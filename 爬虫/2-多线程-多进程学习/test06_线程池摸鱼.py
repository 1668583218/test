# encoding = utf-8
import time
from concurrent.futures import ThreadPoolExecutor


def moyu_time(name, delay, counter):
    while counter:
        print("%s 开始摸鱼 %s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        time.sleep(delay)
        print("%s 结束摸鱼 %s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


# 线程池
if __name__ == '__main__':
    pool = ThreadPoolExecutor(20)
    for i in range(1, 5):
        # submit函数如果第一个参数带形参，就是单线程执行
        # pool.submit(moyu_time('xiaoshuaib' + str(i), 1, 3))
        # submit函数如果第一个参数不带形参，后面的参数就是给第一个参数的值，且可以多线程运行
        pool.submit(moyu_time, ('xiaoshuaib' + str(i)), 5, 1)
