import pymongo
'''
注意：test_data.py文件目的在于给数据库中增加一些带有"已完成"和"待完成"状态的任务数据，
用于测试任务本展示页面中不同任务状态的展示是否实现。
'''

# 连接数据库
client = pymongo.MongoClient()
# 数据库task
db_task = client['task']
# 集合todo
c_todo = db_task['todo']
# 用于测试的数据
data1 = {'subject': '编程', 'content': 'Python实现九九乘法表打印！', 'state': '已完成', 'time': '2022-07-14'}
data2 = {'subject': '编程', 'content': '搭建个人的任务管理项目！', 'state': '待完成', 'time': '2022-07-15'}
data3 = {'subject': '语文', 'content': '学习一首杜甫的诗！', 'state': '已完成', 'time': '2022-08-10'}
data4 = {'subject': '语文', 'content': '默写一首杜甫的诗！', 'state': '待完成', 'time': '2022-08-10'}
data5 = {'subject': '数学', 'content': '完成课本习题！', 'state': '已完成', 'time': '2022-08-17'}
# 任务数据插入数据库
c_todo.insert_one(data1)
c_todo.insert_one(data2)
c_todo.insert_one(data3)
c_todo.insert_one(data4)
c_todo.insert_one(data5)
