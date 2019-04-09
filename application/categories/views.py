from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

@app.route("/categories/new/")
def category_form():
    return render_template("category/new.html")
