from src.admin_views import SecureModelView

class TagView(SecureModelView):
    can_create=True
    can_edit=True
    can_delete=True


    column_list = ['name','news','videos']
    form_columns = ['name']

