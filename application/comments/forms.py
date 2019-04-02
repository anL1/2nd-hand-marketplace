from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class CommentForm(FlaskForm):
    content = StringField("Kommentti:", [validators.InputRequired(), validators.Length(min=3)])

    class Meta:
        csrf = False
