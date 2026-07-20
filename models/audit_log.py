from datetime import datetime
from extensions import db

class AuditLog(db.Model):
    __tablename__ = "audit_log"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, default=0)
    ip = db.Column(db.String(64), nullable=False, default="")
    method = db.Column(db.String(16))
    path = db.Column(db.String(256))
    desc = db.Column(db.String(512), default="")
    create_time = db.Column(db.DateTime, default=datetime.now)
