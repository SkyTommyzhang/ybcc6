from flask import Flask, render_template, request

app = Flask(__name__)


# 科技问答：模拟全部题目数据
data = [
    {
        'id': '1',
        'question': '飞机的发明者是？',
        'options': [
            'A 莱特兄弟',
            'B 波音',
            'C 米格',
            'D 福特'
        ]
    },
    {
        'id': '2',
        'question': '蓝牙技术是一项无线电技术，其传输范围是？',
        'options': [
            'A 5米左右',
            'B 10米左右',
            'C 20米左右',
            'D 100米左右'
        ]
    },
    {
        'id': '3',
        'question': '中国研制的第一台可以每秒运算百亿次的超级计算机叫什么名字？',
        'options': [
            'A 银河三号',
            'B 神州三号',
            'C 风神三号',
            'D 神舟三号'
        ]
    },
    {
        'id': '4',
        'question': '相对论的提出者是？',
        'options': [
            'A 爱因斯坦',
            'B 马克思',
            'C 牛顿',
            'D 马赫'
        ]
    },
    {
        'id': '5',
        'question': '我国第一颗人造地球卫星名字是？',
        'options': [
            'A 酒泉一号',
            'B 东方红一号',
            'C 神州一号',
            'D 中国一号'
        ]
    }
]

q1 = {

    'question': '飞机的发明者是？',
    'options': [
        'A 莱特兄弟',
        'B 波音',
        'C 米格',
        'D 福特'
    ]
}


# 定义路由，设置资源路径为'/page2'
@app.route('/page1')
def page1():
    return render_template('1.html', t_q1=q1)


# 定义路由，设置资源路径为'/page3'
@app.route('/page2')
def page2():
    return render_template('2.html', t_data=data)


# 定义路由，设置资源路径'/result'
@app.route('/result', methods=['POST'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)
