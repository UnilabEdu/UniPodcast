

from src.ext import db
from src.models.base import BaseModel

class Partners(BaseModel):
    __tablename__ = 'partners'

    img = db.Column(db.String,nullable = True)
    link = db.Column(db.String,nullable=True)
