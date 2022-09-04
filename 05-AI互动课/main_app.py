#从flask模块中导入Flask功能
from flask import Flask

#创建服务器对象
app = Flask(__name__)

#定义首页路由结构
#在页面内容中补充一个跳转到“冬天”的a链接
@app.route('/')
def index():
    return '''
        <a href="/spring">春天</a>
        <a href="/summer">夏天</a>
        <a href="/autumn">秋天</a>
        
    '''

#定义"春天"路由结构
@app.route('/spring')
def spring():
    return '''
        <div style="text-align:center">
            <h1>春夜喜雨</h1>
            <h3>唐 杜甫</h3>
            <img src="static/images/spring.png">
            <p>好雨知时节，当春乃发生。</p>
            <p>随风潜入夜，润物细无声。</p>
            <a href="/">返回</a>
        </div>
    '''

#定义"夏天"路由结构
@app.route('/summer')
def summer():
    return '''
        <div style="text-align:center">
            <h1>采莲曲</h1>
            <h3>唐 白居易</h3>
            <img src="static/images/summer.png">
            <p>菱叶萦波荷飐风，荷花深处小船通。</p>
            <p>逢郎欲语低头笑，碧玉搔头落水中。</p>
            <a href="/">返回</a>
        </div>
    '''

#定义"秋天"路由结构
@app.route('/autumn')
def autumn():
    return '''
        <div style="text-align:center">
            <h1>秋夕</h1>
            <h3>唐 杜牧</h3>
            <img src="static/images/autumn.png">
            <p>银烛秋光冷画屏，轻罗小扇扑流萤。</p>
            <p>天阶夜色凉如水，坐看牵牛织女星。</p>
            <a href="/">返回</a>
        </div>
    '''

#定义"冬天"路由结构













#启动服务器
app.run(port=5000, debug=True)