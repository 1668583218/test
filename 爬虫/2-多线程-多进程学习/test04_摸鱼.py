import time


# def moyu_time(name, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s 开始摸鱼 %s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         counter -= 1
#
#
# if __name__ == '__main__':
#     moyu_time('小帅b', 1, 20)

# 仿写摸鱼方法
def moyu(name, delay, counter):
    while counter:
        time.sleep(delay)
        print("{}开始摸鱼{}".format(name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1

if __name__ == "__main__":
    moyu("cao", 1, 20)
