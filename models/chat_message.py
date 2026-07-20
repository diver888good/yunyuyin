from datetime import datetime
from extensions import db

class ChatMessage(db.Model):
    __tablename__ = "chat_message"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content = db.Column(db.Text, default="")
    img_url = db.Column(db.String(256), default="")
    send_time = db.Column(db.DateTime, default=datetime.now)
    is_delete = db.Column(db.Boolean, default=False)
