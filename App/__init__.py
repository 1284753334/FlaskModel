

from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


# def create_app(env):
def create_app():

    #  创建App 对象
    # app = Flask(__name__, template_folder='../templates')
    app = Flask(__name__,static_folder='../static')
    # app = Flask(__name__)

    # 4. 初始化项目配置，新建ext.py
    # app.config.from_object(envs.get(env))
    # 以上配置，我无法映射到数据库，下面的可以映射到数据库，不排除 lunix 和 windows
    # 的原因
    app.config.from_object(envs.get('develop'))
    #  初始化(调用)  非路由  第三方插件
    init_ext(app)

    # 5.路由初始化,新建views.py
    init_blue(app)



    return app






