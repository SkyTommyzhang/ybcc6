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


# 任务首页
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
    client = pymongo.MongoClient()
    db_task = client['task']
    c_todo = db_task['todo']
    c_todo.delete_one(condition)


# "删除任务"路由
@app.route('/delete')
def delete():
    id = request.args['_id']
    condition = {'_id': ObjectId(id)}
    delete_data(condition)

    data = find_data()
    return render_template('index.html', t_data=data)


# 点击完成，数据库修改数据功能(待完成任务->已完成任务)
def finish_data(condition):
    client = pymongo.MongoClient()
    db_task = client['task']
    c_todo = db_task['todo']
    result = c_todo.find_one(condition)
    result['state'] = '已完成'
    result['time'] = get_time()
    c_todo.replace_one(condition, result)


# "完成任务"路由
@app.route('/finish')
def finish():
    id = request.args['_id']
    condition = {'_id': ObjectId(id)}

    client = pymongo.MongoClient()
    db_task = client['task']
    c_todo = db_task['todo']
    # 查询当前_id的任务数据
    result = c_todo.find_one(condition)
    # 修改任务状态
    result['state'] = '已完成'
    # 修改时间
    result['time'] = get_time()
    # 数据库修改数据
    c_todo.replace_one(condition,result)

    # 使用finish_data()功能修改数据库中的数据
    finish_data(condition)

    data = find_data()
    return render_template('index.html', t_data=data)


# 点击撤销，数据库修改数据功能(已完成任务->待完成任务)
def revoke_data(condition):
    client = pymongo.MongoClient()
    db_task = client['task']
    c_todo = db_task['todo']
    result = c_todo.find_one(condition)
    result['state'] = '待完成'
    result['time'] = get_time()
    c_todo.replace_one(condition, result)


# "撤销任务"路由
@app.route('/revoke')
def revoke():
    id = request.args['_id']
    condition = {'_id': ObjectId(id)}
    # 使用revoke_data()功能修改数据库中的数据
    revoke_data(condition)

    data = find_data()
    return render_template('index.html', t_data=data)


app.run(port=5004, debug=True)
