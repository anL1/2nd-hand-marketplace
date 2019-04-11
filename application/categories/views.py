from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.categories.forms import CategoryForm
from application.categories.models import Category

@app.route("/categories/new/", methods=["GET", "POST"])
@login_required
def category_form():
    if request.method == "GET":
        return render_template("category/new.html", form = CategoryForm(), categories = Category.query.all())

    form = CategoryForm(request.form)
    if not form.validate():
        return redirect(url_for('category_form'))

    c = Category(form.name.data)
    db.session().add(c)
    db.session().commit()

    return redirect(url_for('category_form'))
