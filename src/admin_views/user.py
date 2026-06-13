

from src.admin_views import SecureModelView


class UserView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True

    
