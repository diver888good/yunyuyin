from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from business_service.audio_service import AudioService
from business_service.emoji_service import EmojiService
from business_service.voice_demand_service import VoiceDemandService
from business_service.user_service import UserService

admin_bp = Blueprint("admin", __name__)

def admin_check():
    if not current_user.is_authenticated or not UserService.is_admin(current_user.id):
        return jsonify({"code": 403, "msg": "无管理员权限"}), 403

@admin_bp.route("/")
@login_required
def index():
    check = admin_check()
    if check:
        return check
    return render_template("admin/index.html")

@admin_bp.route("/audio/manage")
@login_required
def audio_manage():
    check = admin_check()
    if check:
        return check
    page = int(request.args.get("page", 1))
    pagination = AudioService.page_list(page=page, per_page=15)
    return render_template("admin/audio_manage.html", pagination=pagination)

@admin_bp.route("/audio/edit/<int:aid>", methods=["POST"])
@login_required
def audio_edit(aid):
    check = admin_check()
    if check:
        return check
    title = request.form.get("title")
    category = request.form.get("category")
    is_vip = request.form.get("is_vip") == "on"
    is_show = request.form.get("is_show") == "on"
    AudioService.edit_audio(aid, title=title, category=category, is_vip=is_vip, is_show=is_show)
    flash("音频信息修改成功")
    return redirect(url_for("admin.audio_manage"))

@admin_bp.route("/emoji/manage")
@login_required
def emoji_manage():
    check = admin_check()
    if check:
        return check
    emojis = EmojiService.get_all_show_emoji()
    return render_template("admin/emoji_manage.html", emojis=emojis)

@admin_bp.route("/voice/manage")
@login_required
def voice_manage():
    check = admin_check()
    if check:
        return check
    demands = VoiceDemandService.get_pending_demand()
    return render_template("admin/voice_manage.html", demands=demands)
