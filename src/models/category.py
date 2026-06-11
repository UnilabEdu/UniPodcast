
from src.ext import db
from src.models.base import BaseModel

class Category(BaseModel):
    __tablename__ = 'category'

    category = db.Column(db.String(16))

    videos = db.relationship("Video")
    rubrics = db.relationship("Rubric")