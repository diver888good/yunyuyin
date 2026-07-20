from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from forms.chat_form import ChatMsgForm
from business_service.chat_service import ChatService

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/")
@login_required
def index():
    msgs = ChatService.get_recent_msg()
    return render_template("chat/index.html", msgs=msgs)

@chat_bp.route("/send", methods=["POST"])
@login_required
def send():
    form = ChatMsgForm()
    if form.validate_on_submit():
        ChatService.send_msg(current_user.id, form.content.data)
        return jsonify({"code": 200, "msg": "发送成功"})
    return jsonify({"code": 400, "msg": "消息内容不能为空"})

@chat_bp.route("/api/recent")
def api_recent():
    msgs = ChatService.get_recent_msg()
    res = []
    for m in msgs:
        res.append({
            "user_id": m.user_id,
            "content": m.content,
            "img_url": m.img_url,
            "time": m.send_time.strftime("%m-%d %H:%M")
        })
    return jsonify({"code": 200, "data": res})
