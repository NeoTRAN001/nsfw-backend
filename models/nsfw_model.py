from sqlalchemy import Column, String, Date
from config.database import Base


class NsfwModel(Base):
    __tablename__ = 'nsfw'

    id = Column(String, primary_key=True, index=True)
    image_url = Column(String, index=True)
    prompt = Column(String, index=True)
