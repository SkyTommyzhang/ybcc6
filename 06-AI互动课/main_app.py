from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#给【班级之星】定义路由，设置资源路径为'/star'





#给【班级荣誉墙】定义路由，设置资源路径为'/wall'





#给【运动会风采】定义路由，设置资源路径为'/sport'






app.run(port=5000, debug=True)






























