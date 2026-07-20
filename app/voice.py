from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from forms.voice_form import VoiceDemandForm
from business_service.voice_demand_service import VoiceDemandService
from utils.split_upload import split_save, merge_chunk
from utils.storage_path import get_voice_demand_path
from utils.file_tool import get_file_md5
from tasks.audio_generate_task import create_custom_audio_by_voice_demand
import uuid
import os

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/demand", methods=["POST"])
@login_required
def demand():
    form = VoiceDemandForm()
    if not form.validate_on_submit():
        return jsonify({"code": 400, "msg": "需求描述不能为空"})

    f = request.files.get("voice")
    if not f:
        return jsonify({"code": 400, "msg": "请上传口述语音文件"})

    filename = f"{uuid.uuid4().hex}.wav"
    save_path = os.path.join(get_voice_demand_path(), filename)
    f.save(save_path)

    demand = VoiceDemandService.create_demand(
        user_id=current_user.id,
        voice_file=filename,
        demand_text=form.demand_text.data
    )
    create_custom_audio_by_voice_demand.delay(demand.id)
    return jsonify({"code": 200, "msg": "提交成功，正在生成定制疗愈音频"})

@voice_bp.route("/upload_chunk", methods=["POST"])
@login_required
def upload_chunk():
    file_md5 = request.form.get("md5")
    chunk_idx = int(request.form.get("chunk"))
    chunk_file = request.files["chunk"]
    cache_dir = get_voice_demand_path() + "/temp_chunk"
    split_save(cache_dir, file_md5, chunk_idx, chunk_file.read())
    return jsonify({"code": 200, "msg": "分片上传完成"})
