from flask_restx import  Resource
import math
from src.ext import api
from src.models import News,Category
from src.endpoints.news import news_filter_parser,news_response_model


@api.route('/news')
class NewsApi(Resource):

    @api.expect(news_filter_parser)
    @api.marshal_with(news_response_model)
    def get(self):
        args = news_filter_parser.parse_args()
        category_name = args.get('category')
        title=args.get('title')
        
        page = args.get('page')
        per_page = args.get('per_page')

        news = News.query
        if category_name:
            category_filter = Category.query.filter(Category.category==category_name).first()
            if category_filter:
                news = news.filter(News.category_id==category_filter.id)
            else:
                return {
                    'items':[],
                     'pagination_info':{
                          'page':page,
                          'per_page':per_page,
                          'total':0,
                          'total_pages':0                       
                     }},200

            
        current_page = page 
        if title:
            news=news.filter(News.title.ilike(f"%{title}%"))
        pagination= news.paginate(page=current_page,per_page=per_page,error_out=False)

        return {
            "items": pagination.items,
            "pagination_info": {
            "page": current_page,
            "per_page": per_page,
            "total": pagination.total,
            "total_pages": math.ceil(pagination.total / per_page) if per_page else 0
            }
            }, 200
    
 
