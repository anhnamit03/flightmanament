import json, os
from FlightManament import app, db
from FlightManament.models import  User
import hashlib


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def add_user(name, password, username, **kwargs):
    password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    user = User(name= name.strip(),
                username= username.strip(),
                password=password,
                email= kwargs.get('email'),
                avatar= kwargs.get('avatar'))

    db.session.add(user)
    db.session.commit()


def check_login(username, password):
    if username and password:
        password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)