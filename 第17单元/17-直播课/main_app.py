from flask import Flask, render_template, request
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


# 任务管理项目主页路由
@app.route('/')
def index():
    # 使用find_data()功能获取全部任务数据
    data = find_data()
    return render_template('index.html', t_data=data)


# 任务管理项目'添加任务'路由
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


# 任务管理项目，添加任务'提交表单'路由
@app.route('/save', methods=['POST'])
def save():
    # 获取提交的任务数据
    result = request.form
    data = result.to_dict()
    # 添加任务状态state为'待完成'
    
    # 调用自定义功能get_time()设置任务时间
    data['time'] = get_time()
    # 使用insert_data()功能添加数据到数据库
    insert_data(data)
    return render_template('reminder.html')


app.run(port=5004, debug=True)
