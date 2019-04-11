from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3, max=15)])

    class Meta:
        csrf = False
