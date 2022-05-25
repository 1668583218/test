import os


# # 获得当前工作目录
# print(os.getcwd())
# # 改变当前工作目录
# os.chdir('../')
# # 获得当前工作目录
# print(os.getcwd())

# 获得指定目录下的文件列表
# print(os.listdir("C:/Users/caojingwei/Desktop/新笔记本资料/工作/文档/青岛"))
# 案例: 批量修改文件名
# 创建目录
# os.mkdir("./test01")
# # 改变工作路径
# os.chdir("./test01")
# # 批量创建文件
# for i in range(20):
#     # 以 写入 的形式创建文件
#     file = open("fiel" + str(i), "w")
#     # 关闭文件
#     file.close()
# # 获取目录下的文件
# file = os.listdir()
# print(file)
# # 遍历改名
# for i in file:
#     os.rename(i, "new" + i)
# # 获取目录下的文件
# file = os.listdir()
# print(file)
# print(eval(input("请输入算术题：")))
# a = 1
# print(dir(a))

# 小猫 爱 吃 鱼，小猫 要 喝 水
# class Cat:
#     def __init__(self,name):
#         # 定义用 Cat 类创建的猫对象都有一个 name 的属性
#         self.name = name
#
#     def eat(self):
#         print(self.name + "吃鱼")
#
#     def drink(self):
#         print(self.name + "喝水")
#
# # 使用类名()创建对象的时候，会自动调用初始化方法 __init__
# cat1 = Cat("小猫")
# cat1.eat()
# cat1.drink()
# a = 1
# print("{}".format(a))
# class Cat:
#     def __init__(self, new_name):
#         self.name = new_name
#         print("%s 来了" % self.name)
#
#     def __del__(self):
#         print("%s 去了" % self.name)
#         # tom 是一个全局变量
#
#
# tom = Cat("Tom")
# print(tom.name)
# # del 关键字可以删除一个对象
# del tom
# print("-" * 50)

# class Cat:
#     def __init__(self, new_name):
#         self.name = new_name
#         print("%s 来了" % self.name)
#     def __del__(self):
#         print("%s 去了" % self.name)
#
#     def __str__(self):
#         return "我是小猫：%s" % self.name
#
# tom = Cat("Tom")
# print(tom)

# class Person:
#     """人类"""
#
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return "我的名字叫 %s 体重 %.2f 公斤" % (self.name, self.weight)
#
#     def run(self):
#         """跑步"""
#         print("%s 爱跑步，跑步锻炼身体" % self.name)
#         self.weight -= 0.5
#
#     def eat(self):
#         """吃东西"""
#         print("%s 是吃货，吃完这顿再减肥" % self.name)
#         self.weight += 1
#
#
# xiaoming = Person("小明", 75)
# xiaoming.run()
# xiaoming.eat()
# xiaoming.eat()
# print(xiaoming)
# xiaomei = Person("小美", 50)
# xiaomei.eat()
# xiaomei.run()
# print(xiaomei)

# 家具类
# class HouseItem:
#     def __init__(self, name, area):
#         """
#         :param name: 家具名称
#         :param area: 占地面积
#         """
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "%s的占地面积是%.1f" % (self.name, self.area)
#
#
# # 1. 创建家具
# bed = HouseItem("席梦思", 4)
# chest = HouseItem("衣柜", 2)
# table = HouseItem("餐桌", 1.5)
# print(bed)
# print(chest)
# print(table)
#
# 房子类
# class House:
#     def __init__(self, house_type, area):
#         """
#         :param house_type: 户型
#         :param area: 总面积
#         """
#         self.house_type = house_type
#         self.area = area
#         # 剩余面积默认和总面积一致
#         self.free_area = area
#         # 默认没有任何的家具
#         self.item_list = []
#
#     def __str__(self):
#         return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
#                 % (self.house_type, self.area, self.free_area, self.item_list))
#
#     def add_item(self, item):
#         # 1. 判断家具面积是否大于剩余面积a
#         if item.area > self.free_area:
#             print("剩余面积不足")
#             return
#         # 2. 将家具的名称追加到名称列表中
#         self.item_list.append(item.name)
#         # 3. 计算剩余面积
#         self.free_area -= item.area
#
#
# # 2. 创建房子对象
# my_home = House("两室一厅", 5.5)
# my_home.add_item(bed)
# my_home.add_item(chest)
# my_home.add_item(table)
# print(my_home)

# 枪类
# class Gun:
#     def __init__(self, model):
#         # 枪的类型
#         self.model = model
#         # 默认子弹为0
#         self.bullet_count = 0
#
#     def __str__(self):
#         return "%s的子弹数为%d" % (self.model, self.bullet_count)
#
#     def add_bullet(self, count):
#         # 添加子弹数量
#         self.bullet_count += count
#
#     def shoot(self):
#         # 先判断有无子弹
#         if self.bullet_count == 0:
#             print("没有子弹，无法开枪")
#         else:
#             # 发射子弹
#             self.bullet_count -= 1
#             print("%s 发射子弹[剩余%d]..." % (self.model, self.bullet_count))
#
#
# AK47 = Gun("AK47")
# # AK47.add_bullet(50)
# # AK47.shoot()
#
#
# # 士兵类
# class Soldier:
#     def __init__(self, name):
#         # 姓名
#         self.name = name
#         # 枪，士兵初始没有枪 None 关键字表示什么都没有
#         self.gun = None
#
#     # 分配一把枪
#     def git_gun(self, gun):
#         self.gun = gun
#
#     def fire(self):
#         # 1. 判断士兵是否有枪
#         if self.gun is None:
#             print("%s还没有枪" % self.name)
#             return
#         # 2. 高喊口号
#         print("冲啊...[%s]" % self.name)
#         # 3. 让枪装填子弹
#         self.gun.add_bullet(50)
#         # 4. 让枪发射子弹
#         self.gun.shoot()
#
#
# xusanduo = Soldier("许三多")
# xusanduo.fire()
# xusanduo.git_gun(AK47)
# xusanduo.fire()


# class Women:
#     def __init__(self, name):
#         self.name = name
#         # 不要问女生的年龄
#         self.__age = 18
#     def __secret(self):
#         print("我的年龄是 %d" % self.__age)
# xiaofang = Women("小芳")
# # 私有属性，外部不能直接访问
# # print(xiaofang.__age)
# # 私有方法，外部不能直接调用
# # xiaofang.__secret()
# # 私有属性，外部不能直接访问到
# print(xiaofang._Women__age)
# # 私有方法，外部不能直接调用
# xiaofang._Women__secret()


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s只是简单的玩耍" % self.name)


# class XiaoTianDog(Dog):
#     def game(self):
#         print("%s在天上玩耍" % self.name)
#
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def game_with_dog(self, dog):
#         print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
#         # 让狗玩耍
#         dog.game()
#
# # 1. 创建一个狗对象
# wangcai = Dog("旺财")
# wangcai.game()
# # 2. 创建一个哮天犬对象
# xtq = XiaoTianDog("哮天犬")
# xtq.game()
# # 3. 创建一个小明对象
# xiaoming = Person("小明")
# # 4. 让小明调用和狗玩的方法
# xiaoming.game_with_dog(wangcai)

# class Tool(object):
#     # 使用赋值语句，定义类属性，记录创建工具对象的总数
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         # 针对类属性做一个计数+1
#         Tool.count += 1
#
#     @classmethod
#     def show_tool_count(cls):
#         """显示工具对象的总数"""
#         print("工具对象的总数 %d" % cls.count)
# # 创建工具对象
# tool1 = Tool("斧头")
# tool2 = Tool("榔头")
# tool3 = Tool("铁锹")
# # 知道使用 Tool 类到底创建了多少个对象?
# print("现在创建了 %d 个工具" % Tool.count)
# Tool.show_tool_count()

# @staticmethod
# def 静态方法名():
#     pass

# class Dog(object):
#     # 狗对象计数
#     dog_count = 0
#     @staticmethod
#     def run():
#         # 不需要访问实例属性也不需要访问类属性的方法
#         print("狗在跑...")
#     def __init__(self, name):
#         self.name = name

# 1. 设计一个 Game 类
# 2. 属性：
# 定义一个 类属性 top_score 记录游戏的 历史最高分
# 定义一个 实例属性 player_name 记录 当前游戏的玩家姓名
# 3. 方法：
# 静态方法 show_help 显示游戏帮助信息
# 类方法 show_top_score 显示历史最高分
# 实例方法 start_game 开始当前玩家的游戏
# 4. 主程序步骤
# 1) 查看帮助信息
# 2) 查看历史最高分
# 3) 创建游戏对象，开始游戏

# class Game(object):
#     # 游戏最高分，类属性
#     top_score = 0
#     @staticmethod
#     def show_help():
#         print("帮助信息：让僵尸走进房间")
#     @classmethod
#     def show_top_score(cls):
#         print("游戏最高分是 %d" % cls.top_score)
#     def __init__(self,player_name):
#         self.player_name = player_name
#     def start_game(self):
#         print("[%s] 开始游戏..." % self.player_name)
#         # 使用类名.修改历史最高分
#         Game.top_score=999
# # 1. 查看游戏帮助
# Game.show_help()
# # 2. 查看游戏最高分
# Game.show_top_score()
# # 3. 创建游戏对象，开始游戏
# xiaoming = Game("小明")
# xiaoming.start_game()
# # 4. 游戏结束，查看游戏最高分
# Game.show_top_score()

# class MusicPlayer(object):
#     def __new__(cls, *args, **kwargs):
#     # 如果不返回任何结果，
#         return super().__new__(cls)
#     def __init__(self):
#         print("初始化音乐播放对象")
# player = MusicPlayer()
# print(player)

# class MusicPlayer(object):
#     # 定义类属性记录单例对象引用
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         # 1. 判断类属性是否已经被赋值
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         # 2. 返回类属性的单例引用
#         return cls.instance

# class MusicPlayer(object):
#     # 记录第一个被创建对象的引用
#     instance = None
#     # 记录是否执行过初始化动作
#     init_flag = False
#     def __new__(cls, *args, **kwargs):
#         # 1. 判断类属性是否是空对象
#         if cls.instance is None:
#             # 2. 调用父类的方法，为第一个对象分配空间
#             cls.instance = super().__new__(cls)
#         # 3. 返回类属性保存的对象引用
#         return cls.instance
#     def __init__(self):
#         if not MusicPlayer.init_flag:
#             print("初始化音乐播放器")
#             MusicPlayer.init_flag = True
# # 创建多个对象
# player1 = MusicPlayer()
# print(player1)
# player2 = MusicPlayer()
# print(player2)


# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1 ，对应的代码处理
#     pass
# except (错误类型2, 错误类型3):
#     # 针对错误类型2 和 3，对应的代码处理
#     pass
# except Exception as result:
#     print("未知错误 %s" % result)

# try:
#     num = int(input("请输入整数："))
#     result = 8 / num
#     print(result)
# except ValueError:
#     print("请输入正确的整数")
# except ZeroDivisionError:
#     print("请输入非0的整数")

# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1，对应的代码处理
#     pass
# except 错误类型2:
#     # 针对错误类型2，对应的代码处理
#     pass
# except (错误类型3, 错误类型4):
# # 针对错误类型3 和 4，对应的代码处理
#     pass
# except Exception as result:
#     # 打印错误信息
#     print(result)
# else:
#     # 没有异常才会执行的代码
#     pass
# finally:
#     # 无论是否有异常，都会执行的代码
#     print("无论是否有异常，都会执行的代码")

# try:
#     num = int(input("请输入整数："))
#     result = 8 / num
#     print(result)
# except ValueError:
#     print("请输入正确的整数")
# except ZeroDivisionError:
#     print("除 0 错误")
# except Exception as result:
#     print("未知错误 %s" % result)
# else:
#     print("正常执行")
# finally:
#     print("执行完成，但是不保证正确")

# def demo1():
#     return int(input("请输入一个整数："))
# def demo2():
#     return demo1()
# try:
#     print(demo2())
# except ValueError:
#     print("请输入正确的整数")
# except Exception as result:
#     print("未知错误 %s" % result)

def input_password():
    # 1. 提示用户输入密码
    pwd = input("请输入密码：")
    # 2. 判断密码长度，如果长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3. 密码长度不够，需要抛出异常
    # 1> 创建异常对象 - 使用异常的错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 2> 抛出异常对象
    raise ex


try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as result:
    print("发现错误：%s" % result)
