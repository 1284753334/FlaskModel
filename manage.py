import os
from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app
#  配置 系统环境变量，处于不同的环境下，自动实现系统变量不同
env = os.environ.get('Flask_ENV')

#app = create_app(env)
app = create_app()

manager = Manager(app)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
