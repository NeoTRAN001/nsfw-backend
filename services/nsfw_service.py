from sqlalchemy.orm import Session
from sqlalchemy import text
from models.nsfw_model import NsfwModel


class NSFWService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self, search: str, page: int, limit: int):
        query = self.db.query(NsfwModel)

        if search:
            search_escaped = search.replace("(", "\\(").replace(")", "\\)").replace(" ", "&")

            query = query.filter(
                text("to_tsvector('english', prompt) @@ to_tsquery('english', :search)")
            ).params(search=search_escaped)

        return query.offset((page - 1) * limit).limit(limit).all()
