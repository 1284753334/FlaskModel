from App.ext import db

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16))


class User(db.Model):
    __tablename__ = 'UserModel'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    u_name= db.Column(db.String(64),unique=True)
    u_des = db.Column(db.String(128),nullable=True)


#  模型的继承
class  Animal(db.Model):

    __abstract__=True
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    a_name= db.Column(db.String(32))


class Dog(Animal):
    d_legs = db.Column(db.Integer,default=4)

class Cat(Animal):
    c_food = db.Column(db.String(16),default='fish')


class Customer(db.Model):
        id= db.Column(db.Integer,primary_key=True,autoincrement=True)
        c_name =  db.Column(db.String(32))
        # 把消费者和地址关联 用于获取所有地址  隐形属性
        addresses = db.relationship('Address',backref='Customer',lazy= True)



class Address(db.Model):
        id= db.Column(db.Integer,primary_key=True,autoincrement=True)
        a_position = db.Column(db.String(128))
        #  外键关联
        a_customer_id=db.Column(db.Integer,db.ForeignKey(Customer.id))




