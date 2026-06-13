
from flask import Flask

from src.admin_views import UserView,CategoryView,RubricView,VideoView
from src.config import Config
from src.ext import db,admin
from src.models import User,Category,Rubric,Video

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)

    return app
   
def  register_extensions(app):
    db.init_app(app)
    admin.init_app(app)


    admin.add_view(UserView(User,db.session))
    admin.add_view(CategoryView(Category,db.session))
    admin.add_view(RubricView(Rubric,db.session))
    admin.add_view(VideoView(Video,db.session))
   

