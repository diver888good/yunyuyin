from datetime import datetime
from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(256), default="")
    is_admin = db.Column(db.Boolean, default=False)
    vip_level = db.Column(db.Integer, default=0)
    vip_expire = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Integer, default=1)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def is_vip(self):
        if self.vip_level == 0:
            return False
        if not self.vip_expire:
            return False
        return datetime.now() &lt; self.vip_expire
