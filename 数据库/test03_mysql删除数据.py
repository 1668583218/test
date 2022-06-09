import pymysql

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect(user="root", password="ccbbyy..2030", host="localhost", database="test001")

# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
cursor = db.cursor()

# 插入一条记录
sql = "delete from beautyGirls where age = '%d'" % 18

try:
    cursor.execute(sql)
    # 提交更新，否则不会更新
    db.commit()
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接
db.close()
