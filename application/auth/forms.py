from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3)])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.Length(min=3)])

    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3, max=15)])
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3, max=10)])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=5, max=20), validators.Regexp('.+\d+')])

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=3)])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.DataRequired(), validators.Length(min=5, max=20), validators.Regexp('.+\d+'), validators.EqualTo('confirm', message='Salasanat eivät vastaa')])
    confirm = PasswordField("Salasana uudelleen")

    class Meta:
        csrf = False
