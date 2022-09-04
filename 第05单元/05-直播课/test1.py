# 从flask模块中导入Flask功能
from flask import Flask

# 创建服务器对象
app = Flask(__name__)


# 定义路由结构
@app.route('/')
def index():
    return '<p>Never gonna give you up~</p>'


# 启动服务器
app.run(port=5001, debug=True)

