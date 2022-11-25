from flask import Flask, render_template, request

app = Flask(__name__)

# 根据课程进度选择对应的HTML模板文件：
# 1.html GET请求
# 1.html POST请求
# 2.html 单选按钮


@app.route('/page1')
def page1():
    return render_template("1.html")


@app.route('/page2')
def page2():
    return render_template("2.html")







# 设置接收POST请求
@app.route('/info1')
def info1():
    user = request.args['user']
    pwd = request.args['pwd']
    return '账号：' + user + '<br>' + '密码：' + pwd


@app.route('/info2')
def info2():
    # 获取提交的单选按钮数据
    gender = request.args['gender']
    return '性别:' + gender


app.run(port=5000, debug=True)
