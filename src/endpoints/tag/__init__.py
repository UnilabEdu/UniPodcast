from flask_restx import fields
from src.ext import api

tag_model = api.model('tag', {
                'id': fields.Integer,
                'name': fields.String
         
            })
