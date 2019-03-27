from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.Length(min=3)])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.Length(min=3)])

    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(), validators.Length(min=3)])
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.Length(min=3)])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.Length(min=3)])

    class Meta:
        csrf = False
