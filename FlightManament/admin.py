from FlightManament import app, db
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from FlightManament.models import *
from flask_login import current_user
import utils




class AuthenticateModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id_role.__eq__(7)

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        results = utils.flight_route_stats()
        flight_route_ids = [result.flight_route_id for result in results]
        value_route = [result.flight_count for result in results]
        list_total =[(utils.get_revenue_by_route_flight(result.flight_route_id)) for result in results]


        return self.render('admin/index.html',flight_route_ids=flight_route_ids, value_route=value_route,list_total=list_total)


admin = Admin(app=app, name="SN Airline", template_mode='bootstrap4', index_view=MyAdminIndexView())

admin.add_view(AuthenticateModelView(FlightRole, db.session))
admin.add_view(AuthenticateModelView(Flight, db.session))
admin.add_view(AuthenticateModelView(Plane, db.session))
admin.add_view(AuthenticateModelView(TicketRole, db.session))
admin.add_view(AuthenticateModelView(FlightRoute, db.session))
admin.add_view(AuthenticateModelView(FlightSchedule, db.session))



