from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def hello():
    # 获取提交表单中的城市名称
    city = request.args['city']
    # 获取提交表单中的日期
    date = request.args['date']
    # 获取提交表单中的天气
    weather = request.args['weather']

    # 返回天气信息
    return render_template('weather.html', t_city=city, t_date=date, t_weather=weather)


app.run(port=5003, debug=True)
