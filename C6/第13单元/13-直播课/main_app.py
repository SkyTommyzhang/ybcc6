from flask import Flask, render_template, request

app = Flask(__name__)


# 定义空列表，存放留言数据
data_list = []


# 留言板页面
@app.route('/animal')
def animal():
    # 将变量data_list赋值给模板变量t_datalist
    return render_template('animal.html')


# 提交留言
@app.route('/submit', methods=['POST'])
def submit():
    # 获取提交的表单数据，并转化为字典类型
    info = request.form
    info = info.to_dict()
    # 将当前留言追加到列表中
    # data_list.append(info)
    # print(data_list)
    # 返回成功页面
    return '''
        <p>提交成功</p>
        <a href="/animal">返回主页</a>
    '''


app.run(port=5000, debug=True)
