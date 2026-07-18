from flask_restx import Resource

from src.ext import api
from src.models import Partners
from src.endpoints.partners import partners_model

@api.route('/partners')
class PartnersApi(Resource):
    @api.marshal_with(partners_model,as_list=True)
    def get(self):
        
        partners = Partners.query.all()
        return partners
    