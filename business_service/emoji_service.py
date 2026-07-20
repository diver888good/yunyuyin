from models.system_emoji import SystemEmoji
from extensions import db

class EmojiService:

    @staticmethod
    def get_all_show_emoji():
        return SystemEmoji.query.filter_by(is_show=True).order_by(SystemEmoji.sort).all()
