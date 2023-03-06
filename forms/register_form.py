from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    passwordAgain = PasswordField(validators=[DataRequired()])
    username = StringField(validators=[DataRequired()])
    about = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")
