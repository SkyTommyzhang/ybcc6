from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test.html")

#接收POST请求
@app.route("/result")
def result():
    #获取用户提交的数据
    a1 = request.form['q1']
    a2 = request.form['q2']
    a3 = 
    a4 = 
    a5 = 
    #使用模板变量展示问卷调查结果
    return render_template('result.html',t_a1 = a1,t_a2 = a2,t_a3 = a3,t_a4 = a4,t_a5 = a5,)

app.run(port=5000, debug=True)
