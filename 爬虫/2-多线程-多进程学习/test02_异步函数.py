"""
无异步
"""
# import time
#
#
# def display(num):
#     time.sleep(1)
#     print(num)
#
#
# def main():
#     start = time.time()
#     for i in range(1, 10):
#         display(i)
#     end = time.time()
#     print(f'{end - start:.3f}秒')
#
#
# if __name__ == '__main__':
#     main()


"""
异步改写
"""
import asyncio
import time


async def display(num):
    await asyncio.sleep(1)
    print(num)


def main():
    start = time.time()
    objs = [display(i) for i in range(1, 10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(objs))
    loop.close()
    end = time.time()
    print(f'{end - start:.3f}秒')


if __name__ == '__main__':
    main()
