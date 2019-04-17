from application import db
from application.models import Base

class Product(Base):

    name = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    productCategories = db.relationship("ProductCategory", backref='product', lazy=True)

    def __init__(self, name, content, price):
        self.name = name
        self.content = content
        self.price = price
