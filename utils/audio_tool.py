from mutagen.mp3 import MP3
import os

def get_audio_duration(file_path: str) -> int:
    """获取音频时长（秒）"""
    if not os.path.exists(file_path):
        return 0
    try:
        audio = MP3(file_path)
        return int(audio.info.length)
    except Exception:
        return 0
