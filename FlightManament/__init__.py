
import os
import cloudinary
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
import pyrebase

app = Flask(__name__)
app.secret_key='sbsfusf!$%^&*&%^$$$$%^&'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:anhnam0123@localhost/flightmanament?charset=utf8mb4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8
db = SQLAlchemy(app=app)

cloudinary.config(
            cloud_name = 'del3gk3b3',
            api_key = '258625113394321',
            api_secret = '5eDRz-JGTlkUpJO_Zs7CDaJk2OE'
)

# config auth
firebaseConfig = {
  'apiKey': "AIzaSyB-81olDWdH2wCEla_KTHIbWlxYdBcqK6w",
  'authDomain': "flightmanagement-d989d.firebaseapp.com",
  'projectId': "flightmanagement-d989d",
  'storageBucket': "flightmanagement-d989d.appspot.com",
  'messagingSenderId': "766444659533",
  'appId': "1:766444659533:web:08aa23d67fe25bea740d04",
  'measurementId': "G-0YCW8XPV91"
};

firebase = pyrebase.initialize_app(firebaseConfig)


# login = LoginManager(app=app)
# stripe_key = {
#     "secret_key": os.environ["STRIPE_SECRET_KEY"],
#     "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
#     "price_id": os.environ["STRIPE_PRICE_ID"],
#     "endpoint_secret": os.environ["STRIPE_ENDPOINT_SECRET"],
# }