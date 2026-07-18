from flask_restx import Resource
from src.ext import api

from src.models import Tag
from src.endpoints.tag import tags_model


@api.route('/tags')
class TagsApi(Resource):

    @api.marshal_with(tags_model,as_list=True)
    def get(self):
        tags = Tag.query.all()
        return tags,200
