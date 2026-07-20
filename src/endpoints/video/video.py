import math
from flask_restx import  Resource

from src.ext import api
from src.models import Video,Category
from src.endpoints.video import video_filter_parser,video_model,videos_response_model


@api.route('/video')
class VideoApi(Resource):

    @api.expect(video_filter_parser)
    @api.marshal_with(videos_response_model)
    def get(self):
        args = video_filter_parser.parse_args()
        category_name = args.get('category')
        page = args.get('page')
        per_page = args.get('per_page')

        videos = Video.query
        if category_name:
            category_filter = Category.query.filter(Category.category==category_name).first()
            if category_filter:
                videos = videos.filter(Video.category_id==category_filter.id)
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
        pagination = videos.paginate(page=current_page,per_page=per_page,error_out=False)

        return {
                "items": pagination.items,
                "pagination_info": {
                "page": current_page,
                "per_page": per_page,
                "total": pagination.total,
                "total_pages": math.ceil(pagination.total / per_page) if per_page else 0
                }
                }, 200


@api.route('/slider')
class SliderApi(Resource):
    @api.marshal_with(video_model,as_list = True)
    def get(self):
        slider_videos = Video.query.filter(Video.in_slider == True).all()
        return slider_videos
    


@api.route('/latest_videos')
class LatestVideosApi(Resource):

    @api.marshal_with(video_model, as_list=True)
    def get(self):
        videos = Video.query.order_by(Video.uploaded_at.desc()).limit(2).all()

        return videos,200
