from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.categories.forms import CategoryForm
from application.categories.models import Category

@app.route("/categories/new/", methods=["GET", "POST"])
def category_form():
    if request.method == "GET":
        categories = Category.query.all()
        response = []
        for c in categories:
            productsAmount = len(Category.find_products_in_category(c.id))
            response.append({"name": c.name, "size": productsAmount, "id": c.id})

        return render_template("category/new.html", form = CategoryForm(), categories = response, current_user = current_user)

    form = CategoryForm(request.form)
    if not form.validate():
        return redirect(url_for('category_form'))

    c = Category(form.name.data)
    db.session().add(c)
    db.session().commit()

    return redirect(url_for('category_form'))

@app.route("/categories/<category_id>/")
def category_page(category_id):
    category = Category.query.get(category_id)
    products = Category.find_products_in_category(category_id)

    return render_template("category/category_page.html", category=category, products = products)
