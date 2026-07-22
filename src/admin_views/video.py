from flask_admin.form import ImageUploadField
from flask_admin.contrib.sqla.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.validators import DataRequired,ValidationError
from uuid import uuid4
from markupsafe import Markup
from os import path
from flask_admin.form import ImageUploadField

from src.models.category import Category
from src.admin_views import generate_unique_name
from src.admin_views.base import SecureModelView
from src.models.tag import Tag
from src.models.type import Type


class VideoView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    form_columns = ['category','title','tag','type','description','guests',
        'duration', 'video_link','uploaded_at','img','in_slider'
    ]
    
    form_extra_fields = {
        'img': ImageUploadField(
            base_path=path.join(path.dirname(__file__), '../static/uploads/videos'),
            namegen=generate_unique_name,
            validators=[DataRequired(message="გთხოვთ, ატვირთეთ სურათი")]
        ),
        'category': QuerySelectField(
            'Category',
            query_factory=lambda: Category.query.all(),
            get_label='category',
            allow_blank=True,
            blank_text='აირჩიეთ კატეგორია',
            validators=[DataRequired(message="გთხოვთ, აირჩიოთ კატეგორია")],
            default=None,
        ),
         'tag':QuerySelectMultipleField(
            'tag',
             query_factory=lambda: Tag.query.all(),
             get_label='name',
             default=None,
             validators=[DataRequired()]
                
            ),
        'type':QuerySelectField(
             'Type',
             query_factory=lambda: Type.query.all(),
             get_label='name',
             allow_blank=True,
             blank_text='აირჩიეთ ტიპი',
             validators=[DataRequired(message="გთხოვთ, აირჩიოთ ტიპი")],
             default=None
                          
       ) }
     
    column_list = ['img','category','title','tag','type','uploaded_at']

    column_filters = ['category.category','title','type.name','tag.name']

    column_labels = {
         'title': 'Title',
         'type.name': 'Type',
         'tag.name': 'Tag',
         'type': 'Type',
         'tag': 'Tag' ,
         'category.category': 'Category',
         'category': 'Category'
     }

    column_formatters = {
        'img': lambda v, c, m, p: Markup(
            f'<img src="/static/uploads/videos/{m.img}" width="50" style="border-radius: 4px;">'
        )
    }
  



    