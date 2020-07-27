# from flask_cache import Cache
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# 1.创建 数据库的orm  对象


db=SQLAlchemy()
# 2. 创建 迁移库 对象
migrate = Migrate()
# 缓存到内存中
# cache = Cache(config={'CACHE_TYPE': 'simple'})
# 采用redis 缓存
cache = Cache(config={'CACHE_TYPE': 'redis'})


#  懒加载函数调用的初始化
def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)
    DebugToolbarExtension(app)
    cache.init_app(app)




