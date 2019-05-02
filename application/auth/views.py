from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, SignUpForm, EditForm

from application.products.models import Product

@app.route("/auth/new/", methods=["GET", "POST"])
def auth_create_new():
    if request.method == "GET":
        return render_template("auth/new.html", form = SignUpForm())

    form = SignUpForm(request.form)
    if not form.validate():
        return render_template("auth/new.html", form = form, error = "Salasanan täytyy sisältää väh. 5 merkkiä ja yksi numero")

    users = User.query.all()
    for u in users:
        if u.username == form.username.data:
            return render_template("auth/new.html", form = form, error = "Käyttäjänimi varattu")

    passwordHash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    u = User(form.name.data, form.username.data, passwordHash)
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/login/", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/auth.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/auth.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/auth.html", form = form,
                               error = "Käyttäjää ei olemassa")

    pwCheck = bcrypt.check_password_hash(user.password, form.password.data)

    if pwCheck:
        login_user(user)
        return redirect(url_for("products_index"))
    else:
        return render_template("auth/auth.html", form = form,
                               error = "Virheellinen salasana")

@app.route("/auth/logout/")
def auth_logout():
    logout_user()
    return redirect(url_for("products_index"))

@app.route("/auth/<user_id>/")
def auth_user_page(user_id):
    productList = Product.query.filter_by(account_id = user_id)
    comment_count = User.count_users_comments(user_id)
    return render_template("auth/user_page.html", user = User.query.get(user_id), list = productList, comment_count = comment_count)

@app.route("/auth/<user_id>/edit/", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    if request.method == "GET":
        return render_template("auth/edit_user_information.html", user = User.query.get(current_user.id), form = EditForm())

    form = EditForm(request.form)
    user = User.query.get(user_id)
    if not form.validate():
        return render_template("auth/edit_user_information.html", user = user, form = form)

    user.name = form.name.data
    user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    db.session().commit()

    return redirect(url_for("auth_user_page", user_id=user_id))
