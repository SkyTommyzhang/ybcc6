from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	#返回school.html页面，并为模板变量赋值
    return render_template('school.html', t_bulletin1 = '在这里写下你认为未来学校一天中会发生什么新闻吧！')


app.run(port=5000, debug=True)