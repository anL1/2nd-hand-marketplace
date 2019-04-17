from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, TextAreaField

class ProductForm(FlaskForm):
    name = StringField("Tuotteen nimi:", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3, max=15)])
    content = TextAreaField("Kuvaus:", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3, max=300)])
    price = IntegerField("Hintapyyntö:", [validators.InputRequired(), validators.NumberRange(min=0, max=10000)])

    class Meta:
        csrf = False
