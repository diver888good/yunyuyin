from models.user import User
from extensions import db
from utils.pwd_encrypt import check_password, encrypt_password
from datetime import datetime

class UserService:

    @staticmethod
    def register_user(username: str, email: str, password: str):
        new_user = User(
            username=username,
            email=email,
            password_hash=encrypt_password(password)
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def login_verify(email: str, password: str):
        user = User.query.filter_by(email=email, status=1).first()
        if not user:
            return None
        if not check_password(password, user.password_hash):
            return None
        return user

    @staticmethod
    def update_profile(user_id: int, username: str):
        user = User.query.get(user_id)
        if not user:
            return False
        user.username = username
        user.update_time = datetime.now()
        db.session.commit()
        return True

    @staticmethod
    def is_admin(user_id: int):
        user = User.query.get(user_id)
        if not user:
            return False
        return user.is_admin
