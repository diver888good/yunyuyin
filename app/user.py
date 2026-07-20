from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from forms.user_form import UserProfileForm
from business_service.user_service import UserService

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
@login_required
def index():
    return render_template("user/index.html", user=current_user)

@user_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        ok = UserService.update_profile(current_user.id, username=form.username.data)
        if ok:
            flash("个人资料修改成功")
        return redirect(url_for("user.profile"))
    form.username.data = current_user.username
    return render_template("user/profile.html", form=form)
