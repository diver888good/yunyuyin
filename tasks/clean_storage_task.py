from extensions import celery
from datetime import datetime, timedelta
from utils.cst_upload import cst_delete_file
from models.chat_message import ChatMessage
from models.voice_demand import VoiceDemand
from extensions import db

@celery.task
def clean_expire_storage():
    """
    定时清理过期资源
    1. 聊天室图片7天过期清理
    2. 用户口述语音30天过期清理
    """
    now = datetime.now()

    # 清理7天前聊天图片资源
    expire_chat_time = now - timedelta(days=7)
    expire_imgs = ChatMessage.query.filter(
        ChatMessage.send_time <= expire_chat_time,
        ChatMessage.img_url != ""
    ).all()
    for item in expire_imgs:
        try:
            cst_delete_file(item.img_url)
            item.img_url = ""
        except Exception:
            pass

    # 清理30天前用户口述语音
    expire_voice_time = now - timedelta(days=30)
    expire_voices = VoiceDemand.query.filter(
        VoiceDemand.create_time <= expire_voice_time,
        VoiceDemand.voice_path != ""
    ).all()
    for item in expire_voices:
        try:
            cst_delete_file(item.voice_path)
            item.voice_path = ""
        except Exception:
            pass

    db.session.commit()
    return "clean storage success"
