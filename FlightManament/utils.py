import json, os
from FlightManament import app, db
from FlightManament.models import *
import hashlib
from datetime import datetime
from sqlalchemy.orm import aliased
from geopy.distance import geodesic
from FlightManament import app, db
from FlightManament.models import FlightRouteType
from datetime import datetime, timedelta


def distance(first_place, second_place):
    return geodesic(first_place, second_place)


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def add_user(name, password, username, **kwargs):
    password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    user = User(name=name.strip(),
                username=username.strip(),
                password=password,
                email=kwargs.get('email'),
                avatar=kwargs.get('avatar'))

    db.session.add(user)
    db.session.commit()


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


# Trả về danh sách chuyến bay phù hợp
def get_flight(destination, departure, go_date):
    # Bắt đầu một phiên làm việc với cơ sở dữ liệu
    session = db.session()

    try:
        # Lấy thông tin về bảng FlightRoute
        destination_alias = aliased(Airport)
        departure_alias = aliased(Airport)

        flight_route_info = (
            session.query(FlightRoute.id)
            .join(destination_alias, FlightRoute.destination == destination_alias.id)
            .join(departure_alias, FlightRoute.departure == departure_alias.id)
            .filter(destination_alias.name == destination)
            .filter(departure_alias.name == departure)
            .first()
        )

        if not flight_route_info:
            # Không tìm thấy chuyến bay với các điều kiện đã cho
            return None

        # Chuyển đổi go_date thành định dạng DateTime
        go_date = datetime.strptime(go_date, '%Y-%m-%d')

        # Lấy thông tin về bảng Flight
        flight_id = (
            session.query(Flight.id)
            .filter(Flight.id_flight_route == flight_route_info.id)
            .filter(Flight.start_time >= go_date)
            .first()
        )

        return flight_id

    finally:
        # Đảm bảo đóng phiên làm việc với cơ sở dữ liệu sau khi sử dụng xong
        session.close()


# trả về kí hiệu sân bay
def get_sign(destination, departure):
    session = db.session()

    try:
        # Sử dụng các alias để tham chiếu đến các bảng khi cần thiết
        destination_alias = aliased(Airport, name="destination_airport")
        departure_alias = aliased(Airport, name="departure_airport")

        # Thực hiện truy vấn để lấy thông tin từ bảng Airport cho cả destination và departure
        route_info = (
            session.query(
                destination_alias.sign.label("destination_sign"),
                departure_alias.sign.label("departure_sign")
            )
            .filter(destination_alias.name == destination)
            .filter(departure_alias.name == departure)
            .first()
        )

        if route_info:
            # Chuyển đổi kết quả thành tuple ("fff", "ttt")
            result_tuple = (route_info.destination_sign, route_info.departure_sign)
            return result_tuple
        else:
            return None

    finally:
        session.close()


# trả về id thể loại chuyến bay
def get_type_flight_route(id_flight):
    session = db.session()

    try:
        # Thực hiện truy vấn để lấy id từ bảng FlightRouteType
        type_id = (
            session.query(FlightRouteType.id)
            .join(FlightRoute, FlightRoute.id_flight_route_type == FlightRouteType.id)
            .join(Flight, Flight.id_flight_route == FlightRoute.id)
            .filter(Flight.id == id_flight)
            .first()
        )

        if type_id:
            # Trả về id từ bảng FlightRouteType
            return type_id.id
        else:
            return None

    finally:
        session.close()


def check_login_customer(cccd):
    if cccd:
        # Sử dụng .first() để trả về bản ghi đầu tiên hoặc None nếu không tìm thấy
        customer = Customer.query.filter(Customer.CCCD == cccd).first()
        return customer.id


def get_customer_by_id(user_id):
    return Customer.query.get(user_id)


# Trả về danh sách ghế của máy bay ứng với chuyến bay
def get_seat_ids_by_flight_id_and_type_seat(flight_id, type_seat_id):
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


# Trả về mô tả của thể loại chuyến bay
def get_decription_type_flight_route(id_flight_route_type):
    session = db.session()

    try:
        # Thực hiện truy vấn để lấy mô tả từ bảng FlightRouteType
        type_info = (
            session.query(FlightRouteType.description)
            .filter(FlightRouteType.id == id_flight_route_type)
            .first()
        )

        if type_info:
            # Trả về mô tả từ bảng FlightRouteType
            return type_info.description
        else:
            return None

    finally:
        session.close()


def get_seat_ids_by_flight_id(flight_id):
    session = db.session()

    try:
        # Lấy thông tin về id_plane từ bảng Flight
        id_plane = (
            session.query(Flight.id_plane)
            .filter(Flight.id == flight_id)
            .scalar()
        )

        # Lấy danh sách id ghế từ bảng Seat
        seat_ids = (
            session.query(Seat.id)
            .join(Plane, Plane.id == Seat.id_plane)
            .filter(Plane.id == id_plane)
            .all()
        )

        # Chuyển đổi danh sách kết quả từ tuple sang list
        seat_ids_list = [seat_id[0] for seat_id in seat_ids]

        return seat_ids_list

    finally:
        session.close()


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
