# 导包
from pymongo import MongoClient

# 连接到你的 MongoDB
conn = MongoClient('mongodb://localhost:27017/')
# 创建一个 avIdol 数据库，如果 mongodb 没有会自行创建
db = conn.avIdol
# 往数据库插入一条数据
db.col.insert_one({"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}', 'age': 30})
# 插入多条数据
db.col.insert_many([
    {"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}', 'age': 30},
    {"name": '吉泽明步', 'bwh': '{ "b": 86, "w": 58, "h": 86}', 'age': 35},
    {"name": '桃乃木香奈', 'bwh': '{ "b": 80, "w": 54, "h": 80}', 'age': 22},
    {"name": '西宫梦', 'bwh': '{ "b": 85, "w": 56, "h": 86}', 'age': 22},
    {"name": '松下纱荣子', 'bwh': '{ "b": 88, "w": 57, "h": 86}', 'age': 28}
])
# 查询单条数据
print(db.col.find_one())
# 查询全部数据
for i in db.col.find():
    print(i)
