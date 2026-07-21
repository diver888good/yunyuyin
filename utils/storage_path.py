import os
from dotenv import load_dotenv

load_dotenv()

CST_DOMAIN = os.getenv("CST_DOMAIN", "")
CST_BUCKET = os.getenv("CST_BUCKET", "")

# 固定目录规则（批次14标准）
def get_system_emoji_path():
    return "system_emoji"

def get_chat_img_path():
    return "chat_upload/chat_img"

def get_voice_demand_path():
    return "chat_upload/voice_demand"

def get_custom_audio_path():
    return "custom_audio"

def get_db_backup_path():
    return "db_backup"

def get_temp_cache_path():
    return "temp_cache"

def get_migrate_temp_path():
    return "migrate_temp"

def get_cst_full_url(key: str) -> str:
    """拼接完整CDN地址"""
    if key.startswith("http"):
        return key
    return f"{CST_DOMAIN}/{key}"
