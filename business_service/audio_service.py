from models.audio import Audio
from extensions import db

class AudioService:

    @staticmethod
    def page_list(category="", page=1, per_page=10):
        q = Audio.query.filter_by(is_show=True)
        if category:
            q = q.filter_by(category=category)
        return q.paginate(page=page, per_page=per_page)

    @staticmethod
    def get_audio_by_id(aid: int):
        return Audio.query.get(aid)

    @staticmethod
    def add_play_count(aid: int):
        audio = Audio.query.get(aid)
        if audio:
            audio.play_count += 1
            db.session.commit()

    @staticmethod
    def edit_audio(aid: int, title, category, is_vip, is_show):
        audio = Audio.query.get(aid)
        if not audio:
            return
        audio.title = title
        audio.category = category
        audio.is_vip = is_vip
        audio.is_show = is_show
        db.session.commit()
