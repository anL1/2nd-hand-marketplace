from application import app, db
from flask import render_template, request, redirect, url_for
from application.products.models import Product

@app.route("/products/new/")
def new_ad_form():
    return render_template("products/new_ad.html")

@app.route("/products/", methods=["GET"])
def products_index():
    return render_template("products/products_index.html", productList = Product.query.all())

@app.route("/products/", methods=["POST"])
def product_ad_create():
    p = Product(request.form.get("name"), request.form.get("price"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("products_index"))
