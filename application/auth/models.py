from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    products = db.relationship("Product", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def count_users_comments(account_id):
        stmt = text("select count(comment.id) from comment where account_id = :account_id").params(account_id=account_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        return response
