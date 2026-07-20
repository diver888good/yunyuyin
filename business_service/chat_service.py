from models.chat_message import ChatMessage
from extensions import db
from datetime import datetime

class ChatService:

    @staticmethod
    def send_msg(user_id: int, content: str):
        msg = ChatMessage(
            user_id=user_id,
            content=content,
            send_time=datetime.now()
        )
        db.session.add(msg)
        db.session.commit()

    @staticmethod
    def get_recent_msg(limit=50):
        return ChatMessage.query.filter_by(is_delete=False).order_by(ChatMessage.send_time.desc()).limit(limit).all()
