from flask_restx import Resource
from src.ext import api

from src.models import Tag
from src.endpoints.tag import tag_model


@api.route('/tag')
class TagApi(Resource):

    @api.marshal_with(tag_model,as_list=True)
    def get(self):
        tag = Tag.query.all()
        return tag,200
