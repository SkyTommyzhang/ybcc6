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
    data['state'] = '待完成'
    insert_data(data)
    return render_template('reminder.html')

# 数据库删除数据功能
def delete_data(condition):
    # 连接数据库
    client = pymongo.MongoClient()
    # 数据库schedule
    db_schedule = client['schedule']
    # 集合todo
    c_todo = db_schedule['todo']
    # 数据库删除数据
    c_todo.delete_one(condition)

# "删除任务"路由
@app.route('/delete')
def delete():
    # 获取请求数据
    id = request.args['id']
    # 确认查询条件
    condition = {'_id': ObjectId(id)}
    # 使用delete_data()功能删除数据
    delete_data(condition)
    # 读取数据库中剩余内容
    data = find_data()
    return render_template('index.html', t_data=data)


# 点击完成，数据库修改数据功能(待完成任务->已完成任务)
def finish_data(condition):
    client = pymongo.MongoClient()
    db_task = client['schedule']
    c_todo = db_task['todo']
    # 获取任务对应的一条数据，并将结果保存到变量result中
    # （查询条件储存在变量condition中）
    result = c_todo.find_one(condition)
    # 将数据的完成状态修改为'已完成'
    result['state'] = '已完成'
    # 使用修改完毕的数据替换原数据



# "完成任务"路由
@app.route('/finish')
def finish():
    id = request.args['id']
    condition = {'_id': ObjectId(id)}
    #使用创建finish_data()功能实现数据的修改

    #重新读取修改后的全部数据
    data = find_data()
    return render_template('index.html', t_data=data)

# 点击撤销，数据库修改数据功能(已完成任务->待完成任务)
def revoke_data(condition):
    client = pymongo.MongoClient()
    db_task = client['schedule']
    c_todo = db_task['todo']
    # 获取需要撤销任务对应的数据，并将结果保存到result中
    # （查询条件在变量condition中）
    result = c_todo.find_one(condition)
    result['state'] = '待完成'
    # 使用修改完毕的数据替换原数据
    c_todo.replace_one(condition, result)

# "撤销任务"路由
@app.route('/revoke')
def revoke():
    id = request.args['id']
    condition = {'_id': ObjectId(id)}
    # 使用revoke_data()功能修改数据库中的数据
    revoke_data(condition)
    #重新读取修改后的全部数据
    data = find_data()
    return render_template('index.html', t_data=data)

app.run(port=5006, debug=True)