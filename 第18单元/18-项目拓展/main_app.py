from flask import Flask, render_template, request
from bson.objectid import ObjectId
import pymongo


app = Flask(__name__)

# 数据库查询数据功能
def find_data():
    client = pymongo.MongoClient()
    db_schedule = client['schedule']
    c_todo = db_schedule['todo']
    result = c_todo.find()
    data = list(result)
    return data

# 任务管理项目主页路由
@app.route('/')
def index():
    # 使用find_data()功能获取全部任务数据
    data = find_data()
    return render_template('index.html', t_data=data)

# 数据库添加数据功能
def insert_data(data):
    client = pymongo.MongoClient()
    db_schedule = client['schedule']
    c_todo = db_schedule['todo']
    c_todo.insert_one(data)

# 任务管理项目，添加任务'提交表单'路由
@app.route('/save', methods=['POST'])
def save():
    # 获取提交的任务数据
    result = request.form
    data = result.to_dict()
    insert_data(data)
    return render_template('reminder.html')

# 数据库删除数据功能
def delete_data(condition):
    # 连接数据库
    client = pymongo.MongoClient()
    # 数据库task
    db_schedule = client['schedule']
    # 集合todo
    c_todo = db_schedule['todo']
    # 数据库删除数据，参数为condition


# "删除任务"路由
@app.route('/delete')
def delete():
    # 获取请求数据
    id = request.args['id']
    # 确认查询条件
    condition = {'_id': ObjectId(id)}
    # 使用delete_data()功能删除数据

    # 读取数据库中剩余内容
    data = find_data()
    return render_template('index.html', t_data=data)


app.run(port=5006, debug=True)
