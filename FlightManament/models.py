
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from FlightManament import db
from FlightManament import app
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Airport(BaseModel):
    __tablename__ = "Airport"
    sign = Column(String(5))
    name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    longitude = Column(Float)
    latitude = Column(Float)
    def __str__(self):
        return self.name


class Flight(BaseModel):
    __tablename__ = "Flight"
    start_time = Column(DateTime, nullable=False)
    id_plane = Column(Integer, ForeignKey('Plane.id'), nullable=False)
    id_team_flight = Column(Integer, ForeignKey('TeamFlight.id'), nullable=False)
    id_flight_route = Column(Integer, ForeignKey('FlightRoute.id'), nullable=False)
    is_delete = Column(Integer,  nullable=True)
    def __str__(self):
        return self.name


class FlightRouteType(BaseModel):
    __tablename__ = "FlightRouteType"
    description = Column(String(255))


class Promotion(BaseModel):
    __tablename__ = "Promotions"
    id_flight = Column(Integer, ForeignKey('Flight.id'), primary_key=True, nullable=False)
    value = Column(Integer, nullable=False)


class FlightRole(BaseModel):
    __tablename__ = "FlightRole"
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    value = Column(Integer)


class FlightRoute(BaseModel):
    __tablename__ = "FlightRoute"
    destination = Column(Integer, ForeignKey("Airport.id"), nullable=False)
    departure = Column(Integer, ForeignKey("Airport.id"), nullable=False)
    id_flight_route_type = Column(Integer, ForeignKey("FlightRouteType.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint('destination', 'departure', name='unique_destination_departure'),
    )

class StopPoint(BaseModel):
    __tablename__ = "StopPoint"
    description = Column(String(255))


class FlightSchedule(BaseModel):
    __tablename__ = "FlightSchedule"
    id_stop_point = Column(Integer, ForeignKey("StopPoint.id"), nullable=False)
    id_airport = Column(Integer, ForeignKey("Airport.id"), nullable=False)
    id_flight_route = Column(Integer, ForeignKey("FlightRoute.id"), nullable=False)
    time_stop = Column(Integer)
    description = Column(String(255))



class FlightRoleFlight(BaseModel):
    __tablename__ = "FlightRoleFlight"
    id_flight_role = Column(Integer, ForeignKey('FlightRole.id'), nullable=False)
    id_flight = Column(Integer, ForeignKey("Flight.id"), nullable=False)



class TypeSeat(BaseModel):
    __tablename__ = "TypeSeat"
    name = Column(String(50), nullable=False)
    value = Column(Float, nullable=False)


class Seat(BaseModel):
    __tablename__ = "Seat"
    id_plane = Column(Integer, ForeignKey("Plane.id"), nullable=False)
    id_type_seat = Column(Integer, ForeignKey("TypeSeat.id"), nullable=False)


class Plane(BaseModel):
    __tablename__ = "Plane"
    aircraft_license_plate = Column(String(7), nullable=False)
    flight_speed = Column(Integer)


class TicketStatus(BaseModel):
    __tablename__ = "TicketStatus"
    name = Column(String(50), nullable=False)


class TicketRole(BaseModel):
    __tablename__ = "TicketRole"
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    value = Column(Integer)


class TicketRoleTicket(BaseModel):
    __tablename__ = "TicketRoleTicket"
    id_ticket_role = Column(Integer, ForeignKey("TicketRole.id"), nullable=False)
    id_ticket = Column(Integer, ForeignKey("Ticket.id"), nullable=False)



class Ticket(BaseModel):
    __tablename__ = "Ticket"
    id_seat = Column(Integer, ForeignKey("Seat.id"), nullable=False)
    id_buyer = Column(Integer, ForeignKey("Customer.id"), nullable=False)
    id_passenger = Column(Integer, ForeignKey("Customer.id"), nullable=False)
    id_flight = Column(Integer, ForeignKey("Flight.id"), nullable=False)
    id_ticket_status = Column(Integer, ForeignKey("TicketStatus.id"), nullable=False)
    purchase_time = Column(DateTime)
    employee_responsible = Column(ForeignKey("User.id"))


class Customer(BaseModel):
    __tablename__ = "Customer"
    name = Column(String(255))
    CCCD = Column(String(12), default=None, nullable=False, unique=True)
    gender = Column(Boolean, default=False)
    phone = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)
    birthday = Column(String(50), nullable=False)


class User(BaseModel, UserMixin):
    __tablename__ = "User"
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    name = Column(String(255))
    CCCD = Column(String(12), default=None)
    gender = Column(Boolean, default=False)
    phone = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)
    birthday = Column(String(50), nullable=False)
    id_role = Column(Integer, ForeignKey("Role.id"), nullable=False)
    id_team_flight = Column(Integer, ForeignKey("TeamFlight.id"))


class Role(BaseModel):
    __tablename__ = "Role"
    position = Column(String(50), nullable=False)
    description = Column(String(255))


class Statistical(BaseModel):
    __tablename__ = "Statistical"
    link_statistical = Column(String(255))
    id_user = Column(Integer, ForeignKey("User.id"), nullable=False)


class TeamFlight(BaseModel):
    __tablename__ = "TeamFlight"
    description = Column(String(255))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
