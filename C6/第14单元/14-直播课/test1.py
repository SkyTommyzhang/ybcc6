# 导入pymongo
import pymongo

# 建立连接
client = pymongo.MongoClient()
# 创建数据库
db_store = client['store']
# 创建集合
c_fruit = db_store['fruit']

# 一条数据
data = {'name': '首',
        'kind': 'guy',
        'price': '1145.14',
        'place': '下北沢'}

# 使用insert_one()功能，向集合c_fruit中插入数据data
c_fruit.insert_one(data)
