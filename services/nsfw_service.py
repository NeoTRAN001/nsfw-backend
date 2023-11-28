from sqlalchemy.orm import Session

from models.nsfw_model import NsfwModel


class NSFWService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self):
        return self.db.query(NsfwModel).all()
