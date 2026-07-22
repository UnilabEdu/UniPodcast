from flask_admin.form import ImageUploadField
from uuid import uuid4
from os import path
from markupsafe import Markup
from wtforms.validators import DataRequired

from src.admin_views import SecureModelView,generate_unique_name

class PartnersView(SecureModelView):
    can_create=True
    can_edit=True
    can_delete=True

    form_columns =['link','img']
    column_list = ['link','img']
  

    form_extra_fields = {
        'img': ImageUploadField(
            'Image',
            base_path=path.join(path.dirname(__file__), '../static/uploads/partners'),
            namegen=generate_unique_name,
            validators=[DataRequired(message="გთხოვთ, ატვირთეთ სურათი")]
        )
    }

    column_formatters = {
        'img': lambda v, c, m, p: Markup(
            f'<img src="/static/uploads/partners/{m.img}" width="50" style="border-radius: 4px;">'
        ) if m.img else ""
    }