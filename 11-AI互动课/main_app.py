from flask import Flask, render_template, request

app = Flask(__name__)


# 科技问答：全部题目数据
data = [
    {
        'id': '1',
        'question': '人类首位宇航员是谁？',
        'options': [
            'A 阿姆斯特朗',
            'B 特罗夫斯基',
            'C 加加林',
            'D 奥尔德林'
        ],
        'answer': 'C'
    },
    {
        'id': '2',
        'question': '中国第一批航天员是从什么人员中挑选出来的？',
        'options': [
            'A 特种兵',
            'B 飞行员',
            'C 运动员',
            'D 警察'
        ],
        'answer': 'B'
    },
    {
        'id': '3',
        'question': '我国最南端的航天发射场是？',
        'options': [
            'A 三亚',
            'B 桂林',
            'C 文昌',
            'D 曲靖'
        ],
        'answer': 'C'
    },
    {
        'id': '4',
        'question': '首次着陆月球背面的是？',
        'options': [
            'A 嫦娥四号',
            'B 长征三号',
            'C 嫦娥五号',
            'D 天宫一号'
        ],
        'answer': 'A'
    },
    {
        'id': '5',
        'question': '在_______年，中国实现火星探测。',
        'options': [
            'A 2018',
            'B 2019',
            'C 2020',
            'D 2022'
        ],
        'answer': 'C'
    }
]


# 定义路由，设置资源路径为'/'
@app.route('/')
def index():
    # 返回测试题首页
    return render_template('index.html', t_data=data)


# 定义路由，设置资源路径为'/result'。请求方式：POST
@app.route('/result', methods=['POST'])
def result():
    # 记录正确题目个数
    right = 0
    # 记录错误题目个数

    # 遍历所有题目
    for item in data:
        # 获取用户提交的选择
        choose = request.form[item['id']]
        # 获取正确的答案
        answer = item['answer']

        if answer == choose:
            # 判断：如果正确答案和用户提交的选择相同，则成绩right加1
            right = right + 1
            # 添加flag键，标识正确

            # 判断：如果正确答案和用户提交的选择不相同，则成绩wrong加1


            # 添加flag键，标识错误

        # 给题目字典添加choose键，记录用户选择


    # 根据答对题目数量判断称号
    if right <= 1:
        level = '初级研究员'
    elif right <= 3:
        level = '中级研究员'
    else:
        level = '高级研究员'
    # 返回测试结果页
    return render_template('result.html', t_level=level)


if __name__ == '__main__':
    app.run(port=5000, debug=True)





