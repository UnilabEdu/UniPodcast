
from src.ext import db
from src.models import BaseModel

tag_video = db.Table('tag_video',
    db.Column('video_id',db.Integer,db.ForeignKey('videos.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tags.id'),primary_key=True)
)

class Video(BaseModel):
    __tablename__ = 'videos'
    title = db.Column(db.String(),nullable = False)
    img = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    guests = db.Column(db.String(128), nullable=False)
    duration = db.Column(db.Time, nullable=False)
    uploaded_at = db.Column(db.Date, nullable=False)
    video_link = db.Column(db.String,nullable = True)
    in_slider = db.Column(db.Boolean, default=False)

    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    category = db.relationship('Category',back_populates = 'videos')

    tags = db.relationship('Tag',secondary = tag_video,back_populates='videos')

    type_id = db.Column(db.Integer,db.ForeignKey('types.id'))
    type = db.relationship('Type',back_populates='videos')

    def __str__(self):
        return self.title

























