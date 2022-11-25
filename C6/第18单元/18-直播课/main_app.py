from flask import Flask, render_template, request
from bson.objectid import ObjectId
from datetime import datetime
import pymongo

app = Flask(__name__)


# 数据库查询数据功能
def find_data():
    client = pymongo.MongoClient()
    db_task = client['task']
    c_todo = db_task['todo']
    result = c_todo.find()
    data = list(result)
    return data


@app.route('/')
def index():
    data = find_data()
    return render_template('index.html', t_data=data)


# '添加任务'路由
@app.route('/add')
def add():
    subject = ['编程', '语文', '数学', '英语']
    return render_template('add.html', t_subject=subject)


# 获取当前时间功能
def get_time():
    # 获取当前时间对象
    t = datetime.now()
    # 转换时间格式为字符串
    t = t.strftime('%Y-%m-%d')
    # 返回时间
    return t


# 数据库添加数据功能
def insert_data(data):
    client = pymongo.MongoClient()
    db_task = client['task']
    c_todo = db_task['todo']
    c_todo.insert_one(data)


# '提交表单'路由
@app.route('/save', methods=['POST'])
def save():
    result = request.form
    data = result.to_dict()
    data['state'] = '待完成'
    data['time'] = get_time()
    insert_data(data)
    return render_template('reminder.html')


# 数据库删除数据功能
def delete_data(condition):
    # 连接数据库
    client = pymongo.MongoClient()
    # 获取数据库task
    db_task = client['task']
    # 获取集合todo
    c_todo = db_task['todo']
    # 数据库删除数据
    c_todo.delete_one(condition)


# "删除任务"路由
@app.route('/delete')
def delete():
    # 获取请求数据
    id = request.args['_id']
    # 确认查询条件
    condition = {'_id': ObjectId(id)}
    # 使用delete_data()功能删除数据
    delete_data(condition)
    #  查询删除后的数据库中的所有数据
    data = find_data()
    return render_template('index.html', t_data=data)


app.run(port=5004, debug=True)
