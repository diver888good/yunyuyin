from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired(), Email()])
    password = PasswordField("密码", validators=[DataRequired(), Length(min=6)])

class RegisterForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(), Length(min=2, max=32)])
    email = StringField("邮箱", validators=[DataRequired(), Email()])
    password = PasswordField("密码", validators=[DataRequired(), Length(min=6)])
    repassword = PasswordField("确认密码", validators=[DataRequired(), EqualTo("password", message="两次密码不一致")])

class UserProfileForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(), Length(min=2, max=32)])
