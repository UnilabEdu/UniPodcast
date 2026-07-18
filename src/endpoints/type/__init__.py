from flask_restx import fields
from src.ext import api

type_model = api.model('type', {
                'id': fields.Integer,
                'name': fields.String
                     })

