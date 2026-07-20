from .auth import auth_bp
from .user import user_bp
from .audio import audio_bp
from .chat import chat_bp
from .voice import voice_bp
from .admin import admin_bp

def register_all_blueprint(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(audio_bp, url_prefix="/audio")
    app.register_blueprint(chat_bp, url_prefix="/chat")
    app.register_blueprint(voice_bp, url_prefix="/voice")
    app.register_blueprint(admin_bp, url_prefix="/admin")
