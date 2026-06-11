from src.ext import db
from src.models.base import BaseModel

class Rubric(BaseModel):
    __tablename__ = 'rubric'

    title = db.Column(db.String, nullable=False)
    img = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    uploaded_at = db.Column(db.Date, nullable=False)
    
   

class RubricCategory(BaseModel):
     __tablename__ = 'rubric_category'

     rubric_id = db.Column(db.Integer,db.ForeignKey('rubric.id'))
     category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

     rubric = db.relationship("Rubric")
     category = db.relationship("Category")


