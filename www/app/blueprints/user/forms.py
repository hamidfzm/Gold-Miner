__author__ = 'hamid'

from wtforms import Form, StringField, PasswordField, validators


class Login(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])
