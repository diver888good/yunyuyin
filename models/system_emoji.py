from datetime import datetime
from extensions import db

class SystemEmoji(db.Model):
    __tablename__ = "system_emoji"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emoji_name = db.Column(db.String(64), nullable=False)
    emoji_url = db.Column(db.String(256), nullable=False)
    sort = db.Column(db.Integer, default=0)
    is_show = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
