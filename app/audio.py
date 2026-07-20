from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from business_service.audio_service import AudioService

audio_bp = Blueprint("audio", __name__)

@audio_bp.route("/list")
def audio_list():
    category = request.args.get("category", "")
    page = int(request.args.get("page", 1))
    pagination = AudioService.page_list(category=category, page=page)
    return render_template("audio/list.html", pagination=pagination)

@audio_bp.route("/play/<int:aid>")
def play(aid):
    audio = AudioService.get_audio_by_id(aid)
    if not audio:
        return "音频不存在", 404
    AudioService.add_play_count(aid)
    return render_template("audio/play.html", audio=audio)

@audio_bp.route("/api/list")
def api_list():
    page = int(request.args.get("page", 1))
    pagination = AudioService.page_list(page=page)
    data = []
    for item in pagination.items:
        data.append({
            "id": item.id,
            "title": item.title,
            "category": item.category,
            "duration": item.duration,
            "play_count": item.play_count,
            "audio_url": item.file_path
        })
    return jsonify({"code": 200, "data": data})
