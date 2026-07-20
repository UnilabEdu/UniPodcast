from src.ext import db
from src.models import BaseModel

tag_news = db.Table('tag_news', 
        db.Column('news_id',db.Integer,db.ForeignKey('news.id',),primary_key=True),
        db.Column('tag_id',db.Integer,db.ForeignKey('tags.id',),primary_key=True)
        )

class News(BaseModel):
    __tablename__ = 'news'

    title = db.Column(db.String, nullable=False)
    img = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    news_link = db.Column(db.String,nullable = True)
    uploaded_at = db.Column(db.Date, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category",back_populates='news')

    tag= db.relationship('Tag',secondary=tag_news,back_populates = 'news')

    type_id = db.Column(db.Integer,db.ForeignKey('types.id'))
    type = db.relationship('Type',back_populates ='news')

    def __str__(self):
        return self.title





