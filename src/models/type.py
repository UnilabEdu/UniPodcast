
from src.ext import db
from src.models.base import BaseModel


class Type(BaseModel):
    __tablename__ = 'types'
    name = db.Column(db.String,nullable = True)

    news = db.relationship('News',back_populates = 'type')
    videos = db.relationship('Video',back_populates = 'type')

    def __str__(self):
        return self.name