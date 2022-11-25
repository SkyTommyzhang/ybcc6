from flask import Flask, render_template

app = Flask(__name__)

#菜单数据
menu_data = [
    {
        'dish': '美味汉堡',
        'price': '22元',
        'src': 'static/images/汉堡.png'
    },
    {
        'dish': '健康三明治',
        'price': '17元',
        'src': 'static/images/三明治.png'
    },
    {
        'dish': '热狗',
        'price': '15元',
        'src': 'static/images/热狗.png'
    },
    {
        'dish': '肉夹馍',
        'price': '12元',
        'src': 'static/images/肉夹馍.png'
    },
    {
        'dish':'红烧肉',
        'price': '35元',
        'src': 'static/images/红烧肉.png'
    }

]

@app.route("/")
def menu():
    #模板变量赋值
    return render_template('menu.html', t_menu = menu_data )


app.run(port=5000, debug=True)
