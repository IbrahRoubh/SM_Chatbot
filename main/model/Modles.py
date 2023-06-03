from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'customer'

    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(60), nullable=False)
    c_address = db.Column(db.String(60))
    c_email = db.Column(db.String(60), nullable=False)
    c_phone = db.Column(db.String(60))
    e_storename = db.Column(db.String(250), db.ForeignKey("e_store.name"))
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, name, address, email, phone):
        self.c_name = name
        self.c_address = address
        self.c_email = email
        self.c_phone = phone
        self.e_storename = "Shoies and bag"


class EStore(db.Model):
    __tablename__ = 'e_store'

    name = db.Column(db.String(60), primary_key=True)
    address = db.Column(db.String(60))
    phone_no = db.Column(db.String(60))
    products = db.relationship('Product', backref='e_store', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    p_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(60))
    stock = db.Column(db.Integer)
    price = db.Column(db.Integer)
    size = db.Column(db.String(3))
    color = db.Column(db.String(60))
    photo = db.Column(db.String(250))
    p_code = db.Column(db.String(60), primary_key=True)
    e_storename = db.Column(db.String(250), db.ForeignKey("e_store.name"))


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    o_date = db.Column(db.Date)
    o_shippingaddress = db.Column(db.String(250))
    o_state = db.Column(db.String(250))
    o_total = db.Column(db.Float)
    o_number = db.Column(db.Integer, nullable=False)
    cusid = db.Column(db.Integer, db.ForeignKey('customer.c_id'), nullable=False)
    proid = db.Column(db.Integer, db.ForeignKey('product.p_id'), nullable=False)
