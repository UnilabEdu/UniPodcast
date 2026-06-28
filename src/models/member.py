from src.ext import db
from src.models.base import BaseModel

class Member(BaseModel):
    __tablename__ = 'members'

    name_surname = db.Column(db.String(32),nullable = False)
    role = db.Column(db.String(128),nullable=False)
    in_link = db.Column(db.String())
    img = db.Column(db.String(32), nullable = False)
