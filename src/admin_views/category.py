
from src.admin_views import SecureModelView
from wtforms.validators import DataRequired
class CategoryView(SecureModelView):
   
    can_edit = True
    can_delete = False
    can_create = False

    form_args = {
    'category': {
        'validators': [DataRequired()],
        'allow_blank': True,
        'blank_text': 'აირჩიეთ კატეგორია'
    }
}
  
