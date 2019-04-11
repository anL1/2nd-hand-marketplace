from application import db

class ProductCategory(db.Model):

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False, primary_key=True)

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id
