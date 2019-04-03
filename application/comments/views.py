from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.comments.models import Comment
from application.comments.forms import CommentForm

@app.route("/<product_id>/comments/new/", methods=["POST"])
@login_required
def add_comment(product_id):
    form = CommentForm(request.form)

    if not form.validate():
        return redirect(url_for("single_product_page", product_id = product_id))

    c = Comment(form.content.data)
    c.account_id = current_user.id
    c.product_id = product_id
    db.session().add(c)
    db.session.commit()

    return redirect(url_for("single_product_page", product_id = product_id))

@app.route("/<product_id>/comments/<comment_id>/delete/", methods=["POST"])
@login_required
def delete_comment(comment_id, product_id):
    c = Comment.query.get(comment_id)
    db.session().delete(c)
    db.session().commit()

    return redirect(url_for("single_product_page", product_id = product_id))
