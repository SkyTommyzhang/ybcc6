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
    },
    {
        'id': '6',
        'question': '居里夫人是著名的科学家，她多次获得诺贝尔奖，请问她获得了诺贝尔什么奖项？',
        'options': [
            'A 三次诺贝尔化学奖',
            'B 四次诺贝尔化学奖',
            'C 一次诺贝尔物理奖、一次诺贝尔化学奖',
            'D 两次诺贝尔物理奖'
        ],
        'answer': 'C'
    },
    {
        'id': '7',
        'question': '以下哪个不是中国古代的四大发明？',
        'options': [
            'A 火药',
            'B 地动仪',
            'C 指南针',
            'D 印刷术'
        ],
        'answer': 'B'
    },
    {
        'id': '8',
        'question': '“光年”是什么单位？',
        'options': [
            'A 时间单位',
            'B 长度单位',
            'C 重量单位',
            'D 密度单位'
        ],
        'answer': 'B'
    },
    {
        'id': '9',
        'question': '发明了电话的科学家是？',
        'options': [
            'A 贝尔',
            'B 爱迪生',
            'C 赫兹',
            'D 马克尼'
        ],
        'answer': 'A'
    },
    {
        'id': '10',
        'question': '“给我一个支点，我就能撬起整个地球”是以下谁的名言？',
        'options': [
            'A 法拉第',
            'B 阿基米德',
            'C 麦克斯韦',
            'D 卡文迪许'
        ],
        'answer': 'B'
    },
    {
        'id': '11',
        'question': '以下生活中常见的物品中，什么的设计主要利用了热胀冷缩的原理？',
        'options': [
            'A 汽车轮胎',
            'B 水银温度计',
            'C 电磁炉',
            'D 电池'
        ],
        'answer': 'B'
    },
    {
        'id': '12',
        'question': '托马斯·爱迪生是一位著名的美国科学家、发明家和工程师。以下选项中，哪个是他的发明。',
        'options': [
            'A 自行车',
            'B 计算机',
            'C 留声机',
            'D 汽车'
        ],
        'answer': 'C'
    },
    {
        'id': '13',
        'question': '在以下几种反应中，与其他选项不属于同一类的是？',
        'options': [
            'A 物体在日照下变热',
            'B 灯泡通电发光',
            'C 冰在室温下融化',
            'D 铁栏杆生锈'
        ],
        'answer': 'D'
    },
    {
        'id': '14',
        'question': '英国计算机科学家艾伦·图灵提出了著名的“图灵测试”，用于判断计算机是否具有智能。“图灵测试”是通过什么的方法进行判断的？',
        'options': [
            'A 让两台计算机对话',
            'B 让人类与计算机对话',
            'C 给计算机出题',
            'D 让计算机分辨图片'
        ],
        'answer': 'B'
    },
    {
        'id': '15',
        'question': '人眼看到的苹果是红色的，这是因为？',
        'options': [
            'A 苹果表面会吸收红光',
            'B 苹果会发出红色的光',
            'C 苹果表面反射的光以红色为主',
            'D 红色的光打到了苹果上'
        ],
        'answer': 'C'
    }
]


# 定义路由，设置资源路径为/
@app.route('/question')
def test():
    return render_template('index.html', t_data = data)

# 定义路由，设置资源路径为result
@app.route('/question/result' , methods=['POST'])
def result():
    # 设置变量right表示壮猿成绩
    right = 0
    # for循环遍历题目数据
    for item in data:
        # 获取正确答案
        answer = item['answer']
        # 获取壮猿答案
        choose = request.form[item['id']]
        # 比较正确答案和壮猿答案，相同则壮猿成绩right加1
        if answer == choose:
            right = right + 1

    # 根据right得分情况判断称号
    if right <= 5:
        level = 'level1.png'
    elif right <= 10:
        level = 'level2.png'
    else:
        level = 'level3.png'

    # 返回测试结果页，并将称号level赋值给模板变量t_level
    return render_template('result.html', t_level=level)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
