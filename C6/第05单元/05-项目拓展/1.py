# 从flask模块中导入Flask功能
from flask import Flask

# 创建服务器对象
app = Flask(__name__)


# 定义网页内容
@app.route('/')
# 定义网页内容
def index():
    return '<h1>更换资源路径，进入壮猿的衣橱</h1>'


# 定义资源路径
@app.route('/wardrobe')


# 定义网页内容
def wardrobe():
    # 返回img标签，展示你为壮猿搭配的衣服
    return '''
    		<div>
    			<img src="static/images/壮猿头部.png">
    		</div>

    		'''
# 摆烂了 再见


# 启动服务器
app.run(port=5001, debug=True)
