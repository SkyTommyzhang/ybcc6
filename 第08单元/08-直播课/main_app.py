from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('1.html')


@app.route('/info')
def info():
    # 获取账号数据
    user = request.args['user']
    # 获取密码数据
    pwd = request.args['pwd']
    res = '账号:' + user + '<br>' + '密码:' + pwd
    return res


app.run(port=5000, debug=True)
