from FlightManament import app, db
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView


admin = Admin(app=app, name="E-commerce Administration", template_mode='bootstrap4')


class ProductView(ModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'description']


