# 从flask模块中导入Flask功能
from flask import Flask

# 创建服务器对象
app = Flask(__name__)


# 定义路由结构
@app.route('/')
def index():
    return '<p>Hi!校园生活</p>'


# 定义路由结构
@app.route('/play')
def play():
    return '<p>在操场玩耍</p>'


# 定义路由结构
@app.route('/study')
def study():
    return '<p>在教室学习</p>'


# 启动服务器
app.run(port=5001, debug=True)

