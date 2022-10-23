import pymongo
'''
注意：test_del.py文件的目的在于让同学们练习delete_one()功能的使用，
在数据库中实现正确的删除操作。
'''

# 连接数据库
client = pymongo.MongoClient()
# 获取数据库task
db_task = client['task']
# 获取集合todo
c_todo = db_task['todo']
# 数据库删除数据
c_todo.delete_one({})
