from application import db
from application.models import Base

from sqlalchemy.sql import text

class Category(Base):

    name = db.Column(db.String(144), nullable=False)
    productCategories = db.relationship("ProductCategory", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_products_in_category(category_id):
        stmt = text("select product.id, product.name from product_category, product Where product_category.category_id = :category_id"
        " AND product_category.product_id = product.id"
        " GROUP BY product.id").params(category_id=category_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"product_id": row[0], "product_name": row[1]})

        return response
