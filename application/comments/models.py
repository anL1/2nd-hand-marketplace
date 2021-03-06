from application import db
from application.models import Base

from sqlalchemy.sql import text

class Comment(Base):

    content = db.Column(db.String(300), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, content):
        self.content = content


    @staticmethod
    def find_comments_in_product(product_id):
        stmt = text("SELECT account.id, account.username, comment.content, comment.id FROM"
        " Account, Comment WHERE product_id = :product_id"
        " AND account_id=account.id").params(product_id=product_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"user_id": row[0], "username": row[1], "content": row[2], "comment_id": row[3]})

        return response
