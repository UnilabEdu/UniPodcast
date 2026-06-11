
from src.ext import db
from src.models.base import BaseModel

class User(BaseModel):
    __tablename__ ='user'

    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    