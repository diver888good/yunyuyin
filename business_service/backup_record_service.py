from models.backup_record import BackupRecord
from extensions import db
from datetime import datetime

class BackupRecordService:

    @staticmethod
    def create_record(file_name, file_path, file_size, md5):
        record = BackupRecord(
            file_name=file_name,
            file_path=file_path,
            file_size=file_size,
            md5=md5,
            create_time=datetime.now()
        )
        db.session.add(record)
        db.session.commit()
