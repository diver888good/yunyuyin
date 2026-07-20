import os
import gzip
import subprocess
from datetime import datetime
from app import celery
from utils.cst_upload import cst_upload_file_bytes
from business_service.backup_record_service import BackupRecordService

@celery.task
def db_backup_task():
    """
    每日Neon数据库备份任务
    自动导出 -&gt; 压缩 -&gt; 上传CST db_backup
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        return "db url empty"

    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    dump_name = f"yunyuyin_backup_{date_str}.sql.gz"

    # 导出SQL并压缩
    try:
        result = subprocess.run(
            ["pg_dump", db_url],
            capture_output=True
        )
        sql_data = result.stdout
        zip_data = gzip.compress(sql_data)

        # 上传CST
        cst_path = f"db_backup/{dump_name}"
        url = cst_upload_file_bytes(zip_data, cst_path)

        # 写入备份记录
        BackupRecordService.create_record(
            file_name=dump_name,
            file_path=url,
            file_size=len(zip_data),
            md5=""
        )
        return "backup success"
    except Exception as e:
        return f"backup fail:{str(e)}"
