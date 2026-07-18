from flask_restx import  Resource

from src.ext import api
from src.models import News,Category
from src.endpoints.news import news_filter_parser,news_model 


@api.route('/news')
class NewsApi(Resource):

    @api.expect(news_filter_parser)
    @api.marshal_with(news_model)
    def get(self):
        args = news_filter_parser.parse_args()
        category_name = args.get('category')
        page = args.get('page')
        per_page = args.get('per_page')

        news = News.query
        if category_name:
            category_filter = Category.query.filter(Category.category==category_name).first()
            if category_filter:
                news = news.filter(News.category_id==category_filter.id)
            else:
                return [],200

        current_page = page or 1

        news= news.paginate(page=current_page,per_page=per_page,error_out=False)

        return news.items,200
    
 
