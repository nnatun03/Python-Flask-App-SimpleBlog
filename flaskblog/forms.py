from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',
                           validators=[DataRequired(),Length(min=6,max=30)])
    confrim_password = PasswordField('Confirm password',
                           validators=[DataRequired(),EqualTo('password'),Length(min=6,max=30)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(),Length(min=6,max=30)])
    submit = SubmitField('Login')
    remember = BooleanField('Remember me ?')