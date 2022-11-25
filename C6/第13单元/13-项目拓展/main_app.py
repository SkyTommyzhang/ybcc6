from flask import Flask, render_template, request

app = Flask(__name__)

# 新建列表储存数据
# 物理论坛数据
list_p = []
# 化学论坛数据
list_c = []
# 生物论坛数据
list_b = []


@app.route('/')
def bbs():
    return render_template('bbs.html')


@app.route('/result', methods=['POST'])
def result():
    #获取用户选择的板块数据
    subject = request.form['subject']
    #判断用户选择的板块
    if subject == '物理':
        info = request.form
        #将request.form转换为字典类型
        info = info.to_dict()
        # 将当前留言追加到列表中
        list_p.append(info)
        print(list_p)
        return render_template('physics.html', t_list = list_p)
    elif subject == '化学':
        info = request.form
        #将request.form转换为字典类型
        info = info.to_dict()
        # 将当前留言追加到列表中
        list_c.append(info)
        print(list_c)
        return render_template('chemical.html', t_list = list_c)
    elif subject == '生物':
        info = request.form
        #将request.form转换为字典类型
        info = info.to_dict()
        # 将当前留言追加到列表中
        
        print(list_b)
        return render_template('biology.html', t_list = list_b)


app.run(port=5007, debug=True)
