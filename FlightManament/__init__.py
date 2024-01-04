
import os
import cloudinary
import stripe
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_mail_sendgrid import MailSendGrid

app = Flask(__name__)
app.secret_key = 'sbsfusf!$%^&*&%^$$$$%^&'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:anhnam0123@localhost/flightmanament?charset=utf8mb4'

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://admin:123456@localhost/flightmanament?charset=utf8mb4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8


db = SQLAlchemy(app=app)
cloudinary.config(
            cloud_name='del3gk3b3',
            api_key='258625113394321',
            api_secret='5eDRz-JGTlkUpJO_Zs7CDaJk2OE'
)


# // config login
login_manager = LoginManager(app=app)


stripe_keys = {
    "secret_key": "sk_test_51OAnEvAKLdt3jKp1RnNcu5QaY1Sbfq3YoUYZ52kIO8MyY5aRGmuqU3p6hsvHCGYGA2q2IGD04fG0yOnoae5g1pZu00IpvE82jn",
    "publishable_key": "pk_test_51OAnEvAKLdt3jKp1yBstS2h30XsynBQLsDrM9deUl0CVU1HpWUKxxhAyKMcFFCESIY3D4ooVnjgsP0bZTg6XiJCi00VWgqCJGm",
}
stripe.api_key = stripe_keys["secret_key"]

app.config['MAIL_SENDGRID_API_KEY'] = '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'
mail = MailSendGrid(app)
