from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

# -------------------------定义功能----------------------
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
    res = list(res)
    return res


# -------------------------定义路由结构----------------------
# 留言板页面
@app.route('/board')
def animal():
    # 从集合c_animal中查询留言数据
    data_list = find_data()
    options = ['老虎', '猴子', '大象', '熊猫']
    return render_template('index.html', t_datalist=data_list, t_options=options)


# 提交留言
@app.route('/board/submit', methods=['POST'])
def submit():
    # 获取提交的留言数据，并转为字典类型
    info = request.form
    info = info.to_dict()
    # 插入数据
    insert_data(info)
    # 展示提交结果
    return render_template('reminder.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)

