from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.products.models import Product
from application.products.forms import ProductForm
from application.auth.models import User
from application.comments.models import Comment
from application.comments.forms import CommentForm
from application.categories.models import Category
from application.productCategory.models import ProductCategory

@app.route("/products/new/")
@login_required
def new_ad_form():
    return render_template("products/new_ad.html", form = ProductForm(), categories = Category.query.all())

@app.route("/products/", methods=["GET"])
def products_index():
    return render_template("products/products_index.html", productList = Product.query.all(), user = current_user)

@app.route("/products/", methods=["POST"])
@login_required
def product_ad_create():
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("products/new_ad.html", form = form, categories = Category.query.all())

    p = Product(form.name.data, form.content.data, form.price.data)
    p.account_id = current_user.id
    db.session().add(p)
    db.session().commit()

    categories = request.form.getlist('category_check')
    for c in categories:
        categoryRelation = ProductCategory(p.id, c)
        db.session().add(categoryRelation)
        db.session().commit()

    return redirect(url_for("products_index"))

@app.route("/products/<product_id>/", methods=["GET"])
def single_product_page(product_id):
    p = Product.query.get(product_id)
    user = User.query.get(p.account_id)
    comments = Comment.find_comments_in_product(product_id)
    return render_template("products/product_page.html", product = p, user = user, comments = comments, form = CommentForm(), current_user = current_user)

@app.route("/products/<product_id>/edit/", methods=["GET"])
def product_ad_page(product_id):
    return render_template("products/edit_ad.html", product = Product.query.get(product_id), form = ProductForm())

@app.route("/products/<product_id>/edit/", methods=["POST"])
@login_required
def product_ad_modify(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("products/edit_ad.html", product = Product.query.get(product_id), form = form)

    product.name = form.name.data
    product.content = form.content.data
    product.price = form.price.data

    db.session().commit()

    return redirect(url_for("single_product_page", product_id=product_id))

@app.route("/products/<product_id>/edit/delete/", methods=["POST"])
@login_required
def delete_product_ad(product_id):
    p = Product.query.get(product_id)
    comments = Comment.query.filter_by(product_id = product_id).all()
    categoryRelation = ProductCategory.query.filter_by(product_id = product_id).all()

    for relation in categoryRelation:
        db.session().delete(relation)
        db.session().commit()

    for c in comments:
        db.session().delete(c)
        db.session().commit()

    db.session().delete(p)
    db.session().commit()

    return redirect(url_for("products_index"))
