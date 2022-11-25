import pymongo
'''
注意：test_mongo.py文件目的在于测试环境中是否成功安装MongoDb，与项目部署无关。
'''

client = pymongo.MongoClient()
db = client['test']
c = db['victory']
test_data = {'subject': '编程', 'content': '测试MongoDb！', 'state': '已完成'}
c.insert_one(test_data)
