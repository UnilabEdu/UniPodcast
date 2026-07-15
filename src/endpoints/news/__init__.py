from datetime import datetime
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api



news_filter_parser = RequestParser()
news_filter_parser.add_argument('category',type=str,help='Filter by category_name')
news_filter_parser.add_argument('page',type=int,default=1,help='Page number for pagination')
news_filter_parser.add_argument('per_page',type=int,default =5,help='Number of items per page')


news_model = api.model('rubric', {
                'id': fields.Integer,
                'title': fields.String,
                'img': fields.String,
                'description': fields.String,
                'duration': fields.String,
                'uploaded_at': fields.Date,
                'category_id': fields.Integer

            })
