
import os
import cloudinary
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager


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
# login = LoginManager(app=app)
# stripe_key = {
#     "secret_key": os.environ["STRIPE_SECRET_KEY"],
#     "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
#     "price_id": os.environ["STRIPE_PRICE_ID"],
#     "endpoint_secret": os.environ["STRIPE_ENDPOINT_SECRET"],
# }