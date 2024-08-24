from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, URL


class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class AuthenticationForm(FlaskForm):
    auth_code = StringField('Authentication Code', validators=[DataRequired()])
    submit = SubmitField('Authenticate')


class URLForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Add URL')

