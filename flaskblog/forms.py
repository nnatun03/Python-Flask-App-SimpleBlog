from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',
                           validators=[DataRequired(),Length(min=6,max=30)])
    confirm_password = PasswordField('Confirm password',
                           validators=[DataRequired(),EqualTo('password'),Length(min=6,max=30)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose another one')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please choose another one')
    
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(),Length(min=6,max=30)])
    submit = SubmitField('Login')
    remember = BooleanField('Remember me ?')
    
