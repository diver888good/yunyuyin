# 把 from app import celery 替换为从extensions导入
from extensions import celery
from business_service.voice_demand_service import VoiceDemandService
from utils.storage_path import get_custom_audio_path
from utils.cst_upload import cst_upload_local_file
import os
import uuid

@celery.task
def create_custom_audio_by_voice_demand(demand_id: int):
    """
    根据用户口述语音生成定制疗愈音频（模拟AI生成）
    生产可替换为真实AI语音合成接口
    """
    # 1. 模拟生成成品音频（项目占位逻辑）
    audio_name = f"custom_{uuid.uuid4().hex}.mp3"
    local_save_path = os.path.join(get_custom_audio_path(), audio_name)

    # 2. 上传至CST永久存储
    cst_full_url = cst_upload_local_file(local_save_path, f"custom_audio/{audio_name}")

    # 3. 更新工单状态、绑定成品音频
    VoiceDemandService.finish_demand(demand_id, cst_full_url)
    return {"status": "ok", "audio_url": cst_full_url}
