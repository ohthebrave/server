from main import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)
    addresses = db.relationship('Address', backref='user', lazy=True)
    carts = db.relationship('Cart', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jti = db.Column(db.String(), nullable=True)
    create_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<Token {self.jti}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))  

    # Relationships
    order_items = db.relationship('OrderItem', backref='product', lazy=True)

    

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    orders = db.relationship('Order', backref='cart', lazy=True)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)

    # Relationships
    order_items = db.relationship('OrderItem', backref='order', lazy=True)


class OrderItem(db.Model):
    __tablename__ = 'orderitems'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
