
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api

video_filter_parser = RequestParser()
video_filter_parser.add_argument('category',type=str,help='Filter videos by category name')
video_filter_parser.add_argument('duration',type=str,help='Filter videos by duration ')
video_filter_parser.add_argument('page',type=int,default=1,help='Page number for pagination')
video_filter_parser.add_argument('per_page',type=int,default =5,help='Number of videos per page')

video_model = api.model('video', {
                'id': fields.Integer,
                'title': fields.String,
                'img': fields.String,
                'description': fields.String,
                'guests': fields.String,
                'duration': fields.String,
                'uploaded_at': fields.Date,
                'video_link':fields.String,
                'in_slider': fields.Integer,
                'category_id': fields.Integer

            })
pagination_model = api.model("PaginationInfo", {
                    "page": fields.Integer,
                    "per_page": fields.Integer,
                    "total": fields.Integer,
                    "total_pages": fields.Integer
                                    })


videos_response_model = api.model('Videos',
                {
                'items': fields.List(fields.Nested(video_model)),
                'pagination_info': fields.Nested(pagination_model)
                })



