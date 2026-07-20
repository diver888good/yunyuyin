from models.audit_log import AuditLog
from extensions import db
from datetime import datetime

class AuditService:

    @staticmethod
    def add_log(user_id: int, ip: str, method: str, path: str, desc: str):
        log = AuditLog(
            user_id=user_id,
            ip=ip,
            method=method,
            path=path,
            desc=desc,
            create_time=datetime.now()
        )
        db.session.add(log)
        db.session.commit()
