from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

# -------------------------创建功能----------------------
# 创建功能：将留言数据插入数据库
def insert_data(data):
    client = pymongo.MongoClient()
    db_board = client['board']
    c_animal = db_board['animal']
    c_animal.insert_one(data)


# 创建功能：从数据库中查询留言数据
def find_data():
    client = pymongo.MongoClient()
    db_board = client['board']
    c_animal = db_board['animal']
    res = c_animal.find()
    data_list = list(res)
    return data_list


# -------------------------定义路由结构----------------------
# 留言板页面
@app.route('/animal')
def animal():
    # 从集合c_animal中查询留言数据
    client = pymongo.MongoClient()
    db_board = client['board']
    c_animal = db_board['animal']
    # 从集合c_animal中查询数据
    res = c_animal.find()
    data_list = list(res)
    return data_list
    # 使用find_data()功能查询数据，将查询结果保存在变量data_list中
    data_list = find_data()
    # 展示留言板页面
    return render_template('animal.html', t_datalist=data_list)


# 提交留言
@app.route('/submit', methods=['POST'])
def submit():
    # 获取提交的留言数据，并转为字典类型
    info = request.form
    info = info.to_dict()
    # 使用insert_data()功能，将留言数据info插入到数据库
    insert_data(info)
    # 展示提交结果
    return render_template('result.html')


app.run(port=5000, debug=True)
