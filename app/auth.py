from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from forms.user_form import LoginForm, RegisterForm
from business_service.user_service import UserService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserService.login_verify(form.email.data, form.password.data)
        if user:
            login_user(user)
            return redirect(url_for("user.index"))
        flash("邮箱或密码错误，请重试")
    return render_template("auth/login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        UserService.register_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        flash("注册成功！请前往登录")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("已退出登录")
    return redirect(url_for("auth.login"))
