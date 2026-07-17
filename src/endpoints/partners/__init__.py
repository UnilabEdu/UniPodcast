from flask_restx import fields
from src.ext import api



partners_model = api.model('partners', {
                'id':fields.Integer,
                'link': fields.String,
                'img': fields.String
            })