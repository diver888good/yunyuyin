from datetime import datetime
from extensions import db

class BackupRecord(db.Model):
    __tablename__ = "backup_record"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_name = db.Column(db.String(128), nullable=False)
    file_path = db.Column(db.String(256), nullable=False)
    file_size = db.Column(db.Integer, default=0)
    md5 = db.Column(db.String(64), default="")
    create_time = db.Column(db.DateTime, default=datetime.now)
