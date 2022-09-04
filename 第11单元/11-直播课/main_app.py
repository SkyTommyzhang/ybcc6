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
        ],
        'answer': 'A'
    },
    {
        'id': '2',
        'question': '蓝牙技术是一项无线电技术，其传输范围是？',
        'options': [
            'A 5米左右',
            'B 10米左右',
            'C 20米左右',
            'D 100米左右'
        ],
        'answer': 'B'
    },
    {
        'id': '3',
        'question': '中国研制的第一台可以每秒运算百亿次的超级计算机叫什么名字？',
        'options': [
            'A 银河三号',
            'B 神州三号',
            'C 风神三号',
            'D 神舟三号'
        ],
        'answer': 'A'
    },
    {
        'id': '4',
        'question': '相对论的提出者是？',
        'options': [
            'A 爱因斯坦',
            'B 马克思',
            'C 牛顿',
            'D 马赫'
        ],
        'answer': 'A'
    },
    {
        'id': '5',
        'question': '我国第一颗人造地球卫星名字是？',
        'options': [
            'A 酒泉一号',
            'B 东方红一号',
            'C 神州一号',
            'D 中国一号'
        ],
        'answer': 'B'
    }
]


# 定义路由，设置资源路径为/
@app.route('/')
def test():
    return render_template('index.html', t_data=data)


# 定义路由，设置资源路径为result
@app.route('/result', methods=['POST'])
def result():
    # 设置变量right表示壮猿成绩
    right = 0
    # for循环遍历题目数据，获取答案
    for item in data:
        # 获取正确答案
        answer = item['answer']
        # 获取壮猿答案
        choose = request.form[item['id']]
        # 比较正确答案和壮猿答案，相同则壮猿成绩right加1
        if answer == choose:
            right = right + 1

    # 根据right得分情况判断称号
    if right >= 5:
        level = 'result-window.png'
    elif right >= 4:
        level = 'level3.png'
    elif right >= 2:
        level = 'level2.png'
    elif right >= 1:
        level = 'level1.png'
    else:
        level = 'level0.png'

    # 返回测试结果页，并将称号level赋值给模板变量t_level
    return render_template('result.html', t_level=level)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
