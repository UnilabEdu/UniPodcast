
from src.ext import db
from src.models import BaseModel

class User(BaseModel):
    __tablename__ ='users'

    
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    
    role = db.Column(db.String, default='user')
   