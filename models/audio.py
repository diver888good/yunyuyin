from datetime import datetime
from extensions import db

class Audio(db.Model):
    __tablename__ = "audio"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(32))
    duration = db.Column(db.Integer, default=0)
    file_path = db.Column(db.String(256), nullable=False)
    cover = db.Column(db.String(256), default="")
    play_count = db.Column(db.Integer, default=0)
    is_vip = db.Column(db.Boolean, default=False)
    is_show = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
