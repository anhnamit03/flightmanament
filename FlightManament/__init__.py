
import os
import cloudinary
import stripe
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_mail_sendgrid import MailSendGrid

app = Flask(__name__)
app.secret_key='sbsfusf!$%^&*&%^$$$$%^&'

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:123456@localhost/flightmanament?charset=utf8mb4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8


db = SQLAlchemy(app=app)
cloudinary.config(
            cloud_name = 'del3gk3b3',
            api_key = '258625113394321',
            api_secret = '5eDRz-JGTlkUpJO_Zs7CDaJk2OE'
)


# // config login
login_manager = LoginManager()
login_manager.init_app(app)
# login = LoginManager(app=app)

app.config['MAIL_SENDGRID_API_KEY'] = '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'
mail = MailSendGrid(app)

# stripe_keys = {
#     "secret_key": os.environ["STRIPE_SECRET_KEY"],
#     "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"]
# }
# stripe.api_key = stripe_keys["secret_key"]