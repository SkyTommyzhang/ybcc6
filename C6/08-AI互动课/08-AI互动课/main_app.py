from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('enter.html')


@app.route('/card')
def card():
    # 使用request.args获取用户输入的数据
    receive = request.args['receive']
    send = request.args['send']
    content = request.args['content']

    # 给模板变量赋值
    return render_template('card.html')

app.run(port=5000, debug=True)
