import pymysql

# 使用 connect 方法，传入账号密码，数据库地址，数据库名就可以得到你的数据库对象
db = pymysql.connect(user="root", password="ccbbyy..2030", host="localhost", database="test001")

# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
cursor = db.cursor()

# 比如我们来创建一张数据表
sql = """create table beautyGirls (
   name char(20), age char(20), length char(20)
   )"""
cursor.execute(sql)



# 最后我们关闭这个数据库的连接
db.close()
