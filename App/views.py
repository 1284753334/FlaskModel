import random

from flask import Blueprint, render_template, url_for, request
from sqlalchemy import text, and_, or_, not_

from .ext import db, cache
from .models import Student, Cat, Dog, Customer, Address

blue = Blueprint('blue', __name__, template_folder='../templates',url_prefix='/db')

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/')
def index():
    return 'hello'

@blue.route('/addst/')
def add_st():
    student = Student()
    student.name= "小华%d" % random.randrange(1000)

    db.session.add(student)
    db.session.commit()
    print(db.session)
    print(type(db.session))

    return 'add success'


@blue.route('/addsts/')
def add_sts():
    students = []
    for i in range(10):
        student=Student()
        student.name= '李思%d'% i
        students.append(student)

    db.session.add_all(students)
    db.session.commit()

    return 'add success'


@blue.route('/getstudent/<int:id>')
def get_student(id):

    # student = Student.query.first()
    # student = Student.query.last()
    # student = Student.query.get_or_404(14)
    student = Student.query.get(id)
    print(student)

    return  'Get student'

#查询所有的学生
@blue.route('/getstudents/')
def get_sts():
    students= Student.query.all()

    # for i  in students:
        # print(i.name)

    # return  'successful'
    return  render_template('students_list.html',students = students)


#  删除学生
@blue.route('/deletests/')
def drop_sts():
    student = Student.query.first()
    db.session.delete(student)
    db.session.commit()


    return  'Delete  successful'


#  更新
@blue.route('/update/')
def update():
    student = Student.query.first()
    student.name= 'Tom'
    db.session.add(student)
    db.session.commit()

    return 'update success'

@blue.route('/redir/')
def redir():
   url =  url_for('blue.get_student',id=2)

   return url


@blue.route('/addcat/')
def add_cat():
    cat = Cat()
    cat.a_name= "菠萝"
    cat.c_food='猫粮'
    db.session.add(cat)
    db.session.commit()
    return 'add success'

@blue.route('/adddog/')
def add_dog():
    dog = Dog()
    dog.a_name= "大黄"
    dog.d_legs='5'
    db.session.add(dog)
    db.session.commit()
    return 'add dog success'


@blue.route('/getcat/')
def cat():
    # cats = Cat.query.filter(Cat.id==2)
    # cats = Cat.query.filter(Cat.id > 2)
    # cats = Cat.query.filter(Cat.id.__le__(5)).all()
    # cats = Cat.query.filter(Cat.a_name.contains('黑猫')).all()
    # 跳过第一个 显示2个
    cats= Cat.query.order_by('id').limit(4).offset(5)
    # cats= Cat.query.limit(5).offset(4)



    print(cat)
    print(type(cat))
    return  render_template('cat.html',cats = cats)


@blue.route('/adddogs/')
def add_dogs():
    for i in range(20):
        dog=Dog()
        dog.a_name = '二哈 %d' % random.randrange(10000)
        db.session.add(dog)
    db.session.commit()

    return  '添加成功'


@blue.route('/getdogs/')
def  getdogs():
    page = request.args.get('page',1,type = int)
    per_page = request.args.get('per_page',4, type= int)
    dogs = Dog.query.offset(per_page*(page-1)).limit(per_page)

    return render_template('Dogs.html',dogs=dogs )


#  使用分页器分页
# def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None):
@blue.route('/getdogspage/')
def get_dog_page():
    # dogs = Dog.query.paginate().items
    pagination = Dog.query.paginate()
    per_page = request.args.get('per_page', 4, type=int)

    return render_template('Dogs.html',pagination=pagination,per_page=per_page)




@blue.route('/getcatsfilterby/')
def get_cats_filter_by():
    cats = Cat.query.filter_by(id>5)
    return  render_template('cat.html',cats=cats)



@blue.route('/addcustomer/')
def add_customer():
    customer = Customer()
    customer.c_name='剁手党%d'%random.randrange(10000)
    db.session.add(customer)
    db.session.commit()
    return '消费者创建成功%s' %customer.c_name

@blue.route('/addaddress/')
def add_address():
    address = Address()
    address.a_position= '香格里拉%d' %random.randrange(10000)
    address.a_customer_id= Customer.query.order_by(text('-id')).first().id
    db.session.add(address)
    db.session.commit()
    return '地址创建成功 %s' %address.a_position
# 由地址找到人
@blue.route('/getcustomer/')
def get_customer():
    # 从页面 get 获取参数
    a_id = request.args.get('a_id',type = int)
    address= Address.query.get_or_404(a_id)
    customer = Customer.query.get(address.a_customer_id)

    return  customer.c_name

#由人获取地址
@blue.route('/getaddress/')
def get_address():
    # 从页面 get 获取参数
    c_id = request.args.get('c_id',type = int)
    customer= Customer.query.get_or_404(c_id)

    # addressess = Address.query.filter_by(a_customer_id=customer.id)
    addressess = customer.addresses
    print(addressess)
    print(type(addressess))
    return render_template('address.html',addressess=addressess)

@blue.route('/getaddresseswith/')
@cache.cached(timeout=50)
def  get_addersses():
    #  编号为1的，地址为5 结尾的地址  链式调用
    # addressess = Address.query.filter(Address.a_customer_id.__eq__(1)).filter(Address.a_position.endswith('5'))
    #  改进
    # addressess = Address.query.filter(and_(Address.a_customer_id.__eq__(1),Address.a_position.endswith('5')))
    # addressess = Address.query.filter(or_(Address.a_customer_id.__eq__(1), Address.a_position.endswith('5')))
    addressess = Address.query.filter(not_(or_(Address.a_customer_id.__eq__(1),Address.a_position.endswith('5'))))
    print('从数据库查询')
    return render_template('address.html', addressess=addressess)
















