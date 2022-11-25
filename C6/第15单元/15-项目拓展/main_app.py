from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)


# -------------------------定义功能----------------------
# 创建功能：将留言数据插入数据库
def insert_data(data):
    client = pymongo.MongoClient()
    db_grade = client['grade']
    c_class = db_grade['class']
    c_class.insert_one(data)


# 创建功能：从数据库中查询留言数据
def find_data():
    client = pymongo.MongoClient()
    db_grade = client['grade']
    c_class = db_grade['class']
    # 获取集合中储存的数据
    res = c_class.find()
    # 将数据转换为列表类型
    res = list(res)
    return res


# -------------------------定义路由结构----------------------
# 学生信息录入界面
@app.route('/')
def animal():
    return render_template('student.html')


# 提交信息并插入数据库
@app.route('/submit', methods=['POST'])
def submit():
    # 获取提交的留言数据
    info = request.form
    # 将数据转换为字典类型
    info = info.to_dict()
    # 插入数据
    insert_data(info)
    # 展示提交结果
    return '''
        <p>提交成功</p>
        <a href="/">返回主页</a>
        <a href="/sdata">查看学生信息</a>
    '''


# 查看数据库中的数据
@app.route('/sdata')
def student_data():
    # 使用自己封装的功能，从数据库中读取数据
    datalist = find_data()
    return render_template('sdata.html', s_datalist=datalist)


app.run(port=5001, debug=True)
