from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class CommentForm(FlaskForm):
    content = StringField("Kommentti:", [validators.InputRequired(), validators.Length(min=2)])

    class Meta:
        csrf = False
