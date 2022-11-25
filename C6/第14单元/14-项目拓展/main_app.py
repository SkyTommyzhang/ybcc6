import pymongo

# 建立连接
client = pymongo.MongoClient()
# 创建年级数据库
db_store = client['Grade7']
# 创建班级集合
c_class = db_store['Class1']
# 一条学生数据
student = {'name': 'Millie',
           'gender': 'Female',
           'age': '12',
           'school': 'Sunshine Middle School'
           }

# 向班级集合中插入一条学生数据
c_class.insert_one(student)