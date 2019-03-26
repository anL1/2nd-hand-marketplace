from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application.products.models import Product
from application.products.forms import ProductForm

@app.route("/products/new/")
@login_required
def new_ad_form():
    return render_template("products/new_ad.html", form = ProductForm())

@app.route("/products/", methods=["GET"])
def products_index():
    return render_template("products/products_index.html", productList = Product.query.all())

@app.route("/products/", methods=["POST"])
@login_required
def product_ad_create():
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("products/new_ad.html", form = form)

    p = Product(form.name.data, form.price.data)
    p.account_id = current_user.id 
    db.session().add(p)
    db.session().commit()

    return redirect(url_for("products_index"))

@app.route("/products/<product_id>/", methods=["GET"])
def product_ad_page(product_id):
    return render_template("products/product_ad.html", product = Product.query.get(product_id), form = ProductForm())

@app.route("/products/<product_id>/", methods=["POST"])
def product_ad_modify(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(request.form)
    if not form.validate():
        return render_template("products/product_ad.html", product = Product.query.get(product_id), form = form)

    product.name = form.name.data
    product.price = form.price.data

    db.session().commit()

    return redirect(url_for("products_index"))
