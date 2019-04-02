from application import db
from application.models import Base

class Comment(Base):

    content = db.Column(db.String(300), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, content):
        self.content = content
