from celery import current_app

# 导入所有任务，让Celery自动注册
from . import audio_generate_task
from . import clean_storage_task
from . import db_backup_task

__all__ = [
    "audio_generate_task",
    "clean_storage_task",
    "db_backup_task"
]
