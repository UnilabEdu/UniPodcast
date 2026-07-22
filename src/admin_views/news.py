
from flask_admin.form import ImageUploadField
from flask_admin.contrib.sqla.fields import QuerySelectMultipleField,QuerySelectField
from wtforms.validators import DataRequired
from uuid import uuid4
from os import path
from markupsafe import Markup
from src.admin_views import SecureModelView
from src.models.category import Category
from src.models.tag import Tag
from src.models.type import Type

def generate_unique_name(obj,file):
    extension = path.splitext(file.filename)[1]
    return f"{uuid4()}{extension}"

class NewsView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    form_columns = ['category','title','tag','type','description','duration','news_link','uploaded_at','img']
    form_extra_fields = {
        'img': ImageUploadField(
            base_path=path.join(path.dirname(__file__), '../static/uploads/news'),
            namegen=generate_unique_name,
            validators=[DataRequired(message="გთხოვთ ატვირთოთ სურათი")]
        ),
        'category': QuerySelectField(
            'Category',
            query_factory=lambda: Category.query.all(),
            get_label='category',
            allow_blank=True,
            blank_text='აირჩიეთ კატეგორია',
            validators=[DataRequired(message="გთხოვთ, აირჩიოთ კატეგორია")],
            default=None
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
                        )   }
    
    column_list = ['category','img','title','tag','type','uploaded_at']
    column_filters = ['category.category','title' ,'type.name','tag.name']

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
            f'<img src="/static/uploads/news/{m.img}" width="50" style="border-radius: 4px;">'
        )
    }
  




   
