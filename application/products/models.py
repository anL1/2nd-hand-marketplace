from application import db
from application.models import Base

class Product(Base):

    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    productCategories = db.relationship("ProductCategory", backref='product', lazy=True)

    def __init__(self, name, price):
        self.name = name
        self.price = price
