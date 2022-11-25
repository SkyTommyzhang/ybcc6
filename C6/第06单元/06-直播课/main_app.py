# 从flask模块中导入Flask和render_template功能
from flask import Flask, render_template


# 创建服务器对象
app = Flask(__name__)


# 定义路由，设置资源路径为‘/’
@app.route('/')
# 返回life.html页面,并为模板变量t_name,t_age两个模板变量赋值
def index():
    return render_template('life.html', t_name = '田所浩二', t_age = '114514'),


# 启动服务器
app.run(port=5000, debug=True)
