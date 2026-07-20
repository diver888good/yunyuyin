from models.voice_demand import VoiceDemand
from extensions import db
from utils.storage_path import get_cst_full_url

class VoiceDemandService:

    @staticmethod
    def create_demand(user_id: int, voice_file: str, demand_text: str):
        obj = VoiceDemand(
            user_id=user_id,
            voice_path=voice_file,
            demand_text=demand_text,
            status=0
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    @staticmethod
    def finish_demand(demand_id: int, audio_url: str):
        item = VoiceDemand.query.get(demand_id)
        if not item:
            return
        item.status = 1
        item.result_audio = audio_url
        db.session.commit()

    @staticmethod
    def get_pending_demand():
        return VoiceDemand.query.filter_by(status=0).all()
