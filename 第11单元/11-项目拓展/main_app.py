from flask import Flask, render_template, request

app = Flask(__name__)

#题目数据
data = [
    {
        'id': '1',
        'question': '太阳系中最大的恒星是？',
        'options': [
            'A：太阳',
            'B：月亮',
            'C：地球',
            'D：木星'
        ],
        'answer': 'A'
    },
    {
        'id': '2',
        'question': '地球上最大的海洋是？',
        'options':[
            'A：大西洋',
            'B：北冰洋',
            'C：印度洋',
            'D：太平洋'
        ],
        'answer': 'D'
    },
    {
        'id': '3',
        'question': '人体正常体温为？',
        'options': [
            'A：36摄氏度',
            'B：40摄氏度',
            'C：3.6摄氏度',
            'D：360摄氏度'
        ],
        'answer': 'A'
    },
    {
          'id': '4',
          'question': '叶子逐渐从枝头飘落，那么飘落地面的叶子大多数是哪面朝上？',
          'options': [
              'A: 正面',
              'B: 背面',
              'C: 侧面',
              'D: 立起来'
          ],
          'answer': 'A'
    },
    {
        'id': '5',
        'question': '知识就是力量”是谁的名言？',
        'options': [
            'A: 爱迪生',
            'C: 培根',
            'B: 高尔基',
            'D: 但丁'
        ],
        'answer': 'C'
    },
    {
        'id': '6',
        'question': '中国的首都城市是？',
        'options': [
            'A: 北京',
            'B: 上海',
            'C: 深圳',
            'D: 成都'
        ],
        'answer': 'A'
    },
    {
        'id': '7',
        'question': '小明走路需要10分钟才能到学校，骑单车需要5分钟，如果小明骑单车走到一半路程时单车坏了，后面只能走路去学校，那这次到学校一共要多久？',
        'options': [
            'A: 5分钟',
            'B: 7.5分钟',
            'C: 10分钟',
            'D: 15分钟'
        ],
        'answer': 'B'
    },
    {
        'id': '8',
        'question': '夏季在烈日下工作或运动量过大出汗多时，为预防中暑应多喝？',
        'options': [
            'A: 糖水',
            'B: 糖醋水',
            'C: 盐开水',
            'D: 白开水'
        ],
        'answer': 'C'
    },
    {
        'id': '9',
        'question': '现在中国有多少姓氏？',
        'options': [
            'A: 两万多',
            'B: 一万多',
            'C: 五千多',
            'D: 三千多'
        ],
        'answer': 'C'
    },
    {
        'id': '10',
        'question': '低盐饮食有利于预防什么疾病？',
        'options': [
            'A: 乙型肝炎',
            'B: 糖尿病',
            'C: 高血压',
            'D: 贫血'
        ],
        'answer': 'C'
    }
]


# 路由
@app.route('/')
def index():
    return render_template('index.html', t_data=data)


@app.route('/result', methods=['POST'])
def result():
    #设置变量表示成绩
    score = 0
    for item in data:
        #获取正确答案
        answer = item['answer']
        #获取输入答案
        choose = request.form[item['id']]
        #比较答案，如果答案正确，分数加一
        if answer == choose:
            score = score + 1

    #根据得分确定称号
    level = ''
    #如果得分小于等于三分，获得level1：高手称号
    if score <= 3:
        level = 'level1'
    #如果得分小于等于六分，获得level1：达人称号
    elif score <= 6:
        level = 'level2'
    #如果得分大于六分，获得level1：天才称号
    else score >= 6:
        level = 'level3'

    level += '.png'
    return render_template('result.html', t_level=level)


if __name__ == '__main__':
    app.run(port=5003, debug=True)

