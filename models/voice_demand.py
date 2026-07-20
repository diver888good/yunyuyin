from datetime import datetime
from extensions import db

class VoiceDemand(db.Model):
    __tablename__ = "voice_demand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    voice_path = db.Column(db.String(256), nullable=True)
    demand_text = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, default=0)
    result_audio = db.Column(db.String(256), default="")
    create_time = db.Column(db.DateTime, default=datetime.now)
    finish_time = db.Column(db.DateTime, nullable=True)
