from FlightManament.models import *
from geopy.distance import geodesic
from FlightManament import app, db
from FlightManament.models import FlightRouteType
from datetime import datetime, timedelta
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_
from sqlalchemy import func



def get_name_airport():
    names = Airport.query.with_entities(Airport.name).all()
    name_list = [name[0] for name in names]
    return name_list
def check_login(username, password):
    if username and password:
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_airport_id_by_name(name):
    with app.app_context():
        airport = Airport.query.filter_by(name=name).first()
        if airport:
            return airport.id
        else:
            # Xử lý trường hợp không tìm thấy sân bay, ví dụ: trả về một giá trị mặc định hoặc nâng cao một ngoại lệ.
            return None

def get_flight_route_id_by_two_airport(destination_id, departure_id):
    with app.app_context():
        try:
            route_list = FlightRoute.query.filter(and_(FlightRoute.destination == destination_id, FlightRoute.departure == departure_id)).all()
            return [route.id for route in route_list]
        except NoResultFound:
            # Handle the case when no route with the given airports is found
            return None

def get_flight_id_by_route_and_start_time(route_id, start_time_str):
    with app.app_context():
        try:
            # Convert string start_time to datetime object
            start_time_date = datetime.strptime(start_time_str, "%Y-%m-%d").date()

            # Fetch flights that match the route_id and have the same date part in start_time
            flight_list = Flight.query.filter(
                and_(
                    Flight.id_flight_route == route_id,
                    func.date(Flight.start_time) == start_time_date
                )
            ).all()

            return [flight.id for flight in flight_list]
        except NoResultFound:
            # Handle the case when no route with the given airports is found
            return None

# Trả về danh sách chuyến bay phù hợp
def get_flight(destination, departure, go_date):
    destination_id = get_airport_id_by_name(destination)
    departure_id = get_airport_id_by_name(departure)
    list_routes = get_flight_route_id_by_two_airport(destination_id, departure_id)

    # Initialize an empty list to accumulate flight IDs
    list_id_flight = []

    for route in list_routes:
        # Extend the list with flight IDs for the current route
        list_id_flight.extend(get_flight_id_by_route_and_start_time(route, go_date))

    return list_id_flight


def check_login_customer(cccd):
    if cccd:
        # Sử dụng .first() để trả về bản ghi đầu tiên hoặc None nếu không tìm thấy
        customer = Customer.query.filter(Customer.CCCD == cccd).first()
        return customer.id


def get_customer_by_id(user_id):
    return Customer.query.get(user_id)


# Trả về danh sách ghế của máy bay ứng với chuyến bay
def get_seat_ids_by_flight_id_and_type_seat(flight_id, type_seat_id):
    with app.app_context():
        try:
            # Lấy id_plane từ bảng Flight
            id_plane = db.session.query(Flight.id_plane).filter(Flight.id == flight_id).scalar()

            # Thực hiện truy vấn trong bảng Seat
            seats_query = db.session.query(Seat.id).filter(Seat.id_type_seat == type_seat_id, Seat.id_plane == id_plane)

            # Chuyển kết quả thành danh sách (list)
            seat_ids_list = [seat_id[0] for seat_id in seats_query.all()]

            return seat_ids_list

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc với cơ sở dữ liệu
            db.session.close()


def is_greater_than_hours_from_now(input_datetime_str, hour):
    try:
        # Chuyển đổi chuỗi thành đối tượng datetime
        input_datetime = datetime.strptime(input_datetime_str, "%Y-%m-%d %H:%M:%S")

        # Lấy thời điểm hiện tại
        current_time = datetime.now()

        # Tính ngưỡng thời gian trước
        threshold_time = current_time - timedelta(hours=hour)

        # So sánh và trả về kết quả
        return input_datetime > threshold_time

    except ValueError:
        # Xử lý nếu có lỗi chuyển đổi
        print("Invalid datetime format.")
        return False


# Trả về danh sách các ghế dẫ mua vé
def get_the_list_of_reserved_seats(id_flight):
    with app.app_context():
        try:
            # Lấy danh sách id_seat từ bảng Ticket dựa trên id_flight
            seat_ids = Ticket.query.filter(Ticket.id_flight == id_flight).with_entities(Ticket.id_seat).all()

            # Chuyển kết quả thành danh sách (list)
            seat_ids_list = [seat_id[0] for seat_id in seat_ids]

            return seat_ids_list

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc với cơ sở dữ liệu
            db.session.close()


# Lấy ra số tiền cho thể loại cụ thể
def get_value_by_id_type_seat(id_type_seat):
    with app.app_context():
        try:
            # Lấy giá trị từ bảng TypeSeat dựa trên id_type_seat
            value = TypeSeat.query.filter(TypeSeat.id == id_type_seat).value(TypeSeat.value)

            return value

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc với cơ sở dữ liệu
            db.session.close()


#  Tính giá cho 1 vé
def calculate_for_a_ticket(length, price):
    return length * price


# Trả về tuyến bay tương ứng
def get_flight_route_id_by_flight_id(id_flight):
    with app.app_context():
        try:
            # Lấy id_flight_route từ bảng Flight dựa trên id_flight
            flight_route_id = db.session.query(Flight.id_flight_route).filter(Flight.id == id_flight).scalar()

            return flight_route_id

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc với cơ sở dữ liệu
            db.session.close()


def get_airport_by_id(id_airport):
    with app.app_context():
        try:
            # Lấy đối tượng Airport từ bảng Airport dựa trên id_airport
            airport = db.session.query(Airport).filter(Airport.id == id_airport).first()

            return airport

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc
            db.session.close()


def get_airplane_by_id(id_airplane):
    with app.app_context():
        try:
            # Lấy đối tượng Airport từ bảng Airport dựa trên id_airport
            plane = db.session.query(Plane).filter(Airport.id == id_airplane).first()
            return plane

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc
            db.session.close()


def distance_between_airport(airport_first_place, airport_second_place):
    # Kiểm tra xem có đối tượng sân bay hay không
    if airport_first_place and airport_second_place:
        # Lấy tọa độ của cả hai sân bay
        coordinates_first_place = (airport_first_place.longitude, airport_first_place.latitude)
        coordinates_second_place = (airport_second_place.longitude, airport_second_place.latitude)

        # Tính khoảng cách bằng Geopy
        distance = geodesic(coordinates_first_place, coordinates_second_place).km
        return distance
    else:
        print("Error: Invalid airport objects.")
        return None


def get_all_type_seat_ids():
    with app.app_context():
        try:
            # Lấy danh sách id của bảng TypeSeat
            type_seat_ids = db.session.query(TypeSeat.id).all()

            # Chuyển kết quả thành danh sách (list)
            type_seat_ids_list = [type_seat_id[0] for type_seat_id in type_seat_ids]

            return type_seat_ids_list

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc với cơ sở dữ liệu
            db.session.close()


def calculate_length_flight(destination, departure, flight_schedules):
    length = 0

    if len(flight_schedules) == 0:
        length = distance_between_airport(destination, departure)
    elif len(flight_schedules) == 1:
        length = distance_between_airport(destination, get_airport_by_id(flight_schedules)[0].id_airport) \
                 + distance_between_airport(departure, get_airport_by_id(flight_schedules)[0].id_airport)
    elif len(flight_schedules) == 2:
        length = distance_between_airport(get_airport_by_id(flight_schedules[1].id_airport),
                                          get_airport_by_id(flight_schedules[0].id_airport))
        for i in range(len(flight_schedules)):

            if flight_schedules[i].id_stop_point == 1:
                length += distance_between_airport(destination, get_airport_by_id(flight_schedules[i].id_airport))
            if flight_schedules[i].id_stop_point == 2:
                length += distance_between_airport(departure, get_airport_by_id(flight_schedules[i].id_airport))

    return length


def get_flight_route_by_id(id_flight_router):
    with app.app_context():
        return FlightRoute.query.get(id_flight_router)

def get_type_flight_description(id_type_flight):
    with app.app_context():
        return FlightRouteType.query.get(id_type_flight).description


def get_flight_schedules_by_route_id(id_flight_route):
    with app.app_context():
        return FlightSchedule.query.filter_by(id_flight_route=id_flight_route).all()


def get_stop_times(flight_schedules):
    stop_time = 0
    if flight_schedules:
        for flight_schedule in flight_schedules:
            stop_time += flight_schedule.time_stop
    return stop_time


def get_flight_by_id(id_flight):
    with app.app_context():
        return db.session.query(Flight).filter(Flight.id == id_flight).first()


def extract_hour_minute(datetime_str):
    try:
        hour_minute_str = datetime_str.strftime("%H:%M")

        return hour_minute_str

    except ValueError:
        # Xử lý nếu có lỗi chuyển đổi
        print("Invalid datetime format.")
        return None

def convert_minutes_to_hours_and_minutes(minutes):
    # Tính số giờ và số phút
    hours = minutes // 60
    remaining_minutes = minutes % 60

    # Tạo chuỗi kết quả
    result_str = f"{hours} giờ {remaining_minutes} phút"

    return result_str


def calculate_end_time(start_time, time_fly):
    # Chuyển đổi thời gian bắt đầu từ chuỗi thành đối tượng datetime
    start_datetime = datetime.strptime(start_time, "%H:%M")

    # Tính thời gian bay thành đối tượng timedelta
    fly_duration = timedelta(minutes=time_fly)

    # Tính thời gian kết thúc bằng cách cộng thời gian bắt đầu và thời gian bay
    end_datetime = start_datetime + fly_duration

    # Chuyển đối tượng datetime thành chuỗi định dạng giờ:phút
    end_time_str = end_datetime.strftime("%H:%M")

    return end_time_str


def get_ticketrole_values():
    with app.app_context():
        try:
            # Lấy danh sách giá trị từ cột 'value' trong bảng 'ticketrole'
            values = db.session.query(TicketRole.value).all()

            # Chuyển đổi kết quả từ list của các tuple thành list của các giá trị
            values_list = [value[0] for value in values]

            return values_list

        except Exception as e:
            # Xử lý lỗi nếu có
            print(f"Error: {e}")
            return None
        finally:
            # Đóng phiên làm việc
            db.session.close()


class info_book_ticket(object):
    def __init__(self,start_time, destination_sign, departure_sign, all_time_fly,
                end_time,list_stop_points, list_seat_rank_1, list_seat_rank_2, price_seat_rank_1,
                price_seat_rank_2,list_seated,type_flight,id_flight):
        self.start_time = start_time
        self.destination_sign = destination_sign
        self.departure_sign = departure_sign
        self.all_time_fly =all_time_fly
        self.end_time = end_time
        self.list_stop_points = list_stop_points
        self.list_seat_rank_1 = list_seat_rank_1
        self.list_seat_rank_2 = list_seat_rank_2
        self.price_seat_rank_1 = price_seat_rank_1
        self.price_seat_rank_2 = price_seat_rank_2
        self.list_seated = list_seated
        self.type_flight = type_flight
        self.id_flight = id_flight


# Function cho việc đặt vé
def reder_interface_for_book_ticket_customer(id_flight):

    id_flight_router = get_flight_route_id_by_flight_id(id_flight)
    flight_router = get_flight_route_by_id(id_flight_router)
    flight = get_flight_by_id(id_flight)
    destination = get_airport_by_id(flight_router.destination)
    departure = get_airport_by_id(flight_router.departure)
    flight_schedules = get_flight_schedules_by_route_id(id_flight_router)
    stop_time = get_stop_times(flight_schedules)
    list_seat_rank_1 = get_seat_ids_by_flight_id_and_type_seat(id_flight, 1)
    list_seat_rank_2 = get_seat_ids_by_flight_id_and_type_seat(id_flight, 2)
    list_seated = get_the_list_of_reserved_seats(id_flight)
    length = calculate_length_flight(destination, departure, flight_schedules)
    plane = get_airplane_by_id(flight.id_plane)
    price_seat_rank_2 = int(get_value_by_id_type_seat(1) * length)
    price_seat_rank_1 = int(get_value_by_id_type_seat(2) * length)
    start_time = extract_hour_minute(flight.start_time)
    all_time_fly = convert_minutes_to_hours_and_minutes(stop_time+int(length/plane.flight_speed*60))
    end_time = calculate_end_time(start_time,stop_time+int(length/plane.flight_speed*60))
    type_flight = get_type_flight_description(flight_router.id_flight_route_type)
    stop_point_1 = None
    stop_point_2 = None


    for schedule in flight_schedules:
        if schedule.id_stop_point == 1:
            stop_point_1 = get_airport_by_id(schedule.id_airport).name
        if schedule.id_stop_point == 2:
            stop_point_2 = get_airport_by_id(schedule.id_airport).name

    list_stop_points = [stop_point_1, stop_point_2]



    book_ticket_info = info_book_ticket(start_time, destination.sign, departure.sign, all_time_fly,
                     end_time,list_stop_points, list_seat_rank_1, list_seat_rank_2, price_seat_rank_1,
                     price_seat_rank_2,list_seated,type_flight,flight.id)
    return book_ticket_info


def get_all_roles():
    with app.app_context():
        roles = Role.query.all()
        roles_list = [role.__dict__ for role in roles]
        roles_list = [{key: value for key, value in role.items() if key != '_sa_instance_state'} for role in roles_list]
        return roles_list
        db.session.close()


def get_all_team_flight():
    with app.app_context():
        roles = TeamFlight.query.all()
        team_flight = [team.__dict__ for team in roles]
        team_flight = [{key: value for key, value in team.items() if key != '_sa_instance_state'} for team in team_flight]
        return team_flight
        db.session.close()



def check_login_by_email(email):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        return user



def add_user(username, password, avatar, name, CCCD, gender, phone, email, birthday, id_role, id_team_flight ):
    user = User(username= username.strip(),
                password=password,
                avatar=avatar,
                name=name,
                CCCD=CCCD,
                gender=gender,
                phone=phone,
                email=email,
                birthday=birthday,
                id_role=id_role,
                id_team_flight=id_team_flight)
    db.session.add(user)
    db.session.commit()


def add_customer(name, CCCD, gender, phone, email, birthday ):
    customer = Customer(name=name,
                        CCCD=CCCD,
                        gender=gender,
                        phone=phone,
                        email=email,
                        birthday=birthday)
    with app.app_context():
        db.session.add(customer)
        db.session.commit()


def get_id_role(position):
    with app.app_context():
        role = Role.query.filter_by(position=position).first()
        return role.id


def get_id_customer(CCCD):
    with app.app_context():
        customer = Customer.query.filter_by(CCCD=CCCD).first()
        return customer.id


def add_team_flight(description):
    team_flight = TeamFlight(description =description)
    db.session.add(team_flight)
    db.session.commit()


def add_ticket(id_seat,id_buyer,id_passenger,id_flight,id_ticket_status, **kwargs):
    employee_responsible = kwargs.get('employee_responsible', None)
    ticket = Ticket(
        id_seat=id_seat,
        id_buyer=id_buyer,
        id_passenger=id_passenger,
        id_flight=id_flight,
        id_ticket_status=id_ticket_status,
        purchase_time= datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'),
        employee_responsible=employee_responsible
    )
    db.session.add(ticket)
    db.session.commit()


def get_flight_by_year_and_month(year, month):
    with app.app_context():
        # Lấy danh sách các chuyến bay có trường start_time thuộc về năm và tháng đã chỉ định
        flights = Flight.query.filter(
            db.extract('year', Flight.start_time) == year,
            db.extract('month', Flight.start_time) == month
        ).all()

        return flights


def flight_route_stats():
    with app.app_context():
        return FlightRoute.query.join(Flight, Flight.id_flight_route.__eq__(FlightRoute.id), isouter=True) \
                                .add_column(FlightRoute.id.label('flight_route_id')) \
                                .add_column(func.count(Flight.id).label('flight_count')) \
                                .group_by(FlightRoute.id) \
                                .all()

def revenue_by_flight_id(flight_id):
    total = 0
    with app.app_context():
        try:
            tickets = Ticket.query.filter(Ticket.id_flight == flight_id).all()
            list_seat = [ticket.id_seat for ticket in tickets]
            a = reder_interface_for_book_ticket_customer(flight_id)
            for item in list_seat:
                if item in a.list_seat_rank_2:
                    total += a.price_seat_rank_2
                elif item in a.list_seat_rank_1:
                    total += a.price_seat_rank_1
        except Exception as e:

            total = 0  # Hoặc giá trị mặc định khác phù hợp với trường hợp lỗi của bạn
    return total

def get_revenue_by_route_flight(id_router_flight):
    total = 0
    with app.app_context():
        flights = Flight.query.filter(Flight.id_flight_route == id_router_flight).all()
        if flights:
            id_flights = [flight.id for flight in flights]
            for item in id_flights:
                total += revenue_by_flight_id(item)

    return total






if __name__ == '__main__':
    print(reder_interface_for_book_ticket_customer(10).price_seat_rank_1)




