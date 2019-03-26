from flask import render_template, request, redirect, url_for
from application import app
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login/", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/auth.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/auth.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/auth.html", form = form,
                               error = "No such username or password")

    return redirect(url_for("products_index"))
