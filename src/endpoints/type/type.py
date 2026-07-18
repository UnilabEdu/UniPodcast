from flask_restx import Resource
from src.ext import api

from src.models import Type
from src.endpoints.type import type_model

@api.route('/type')
class TypeApi(Resource):
    
    @api.marshal_with(type_model,as_list =True)
    def get(self):
        types = Type.query.all()
        return types,200