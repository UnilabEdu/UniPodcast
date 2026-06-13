
from src.admin_views import SecureModelView

class CategoryView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True

  

   