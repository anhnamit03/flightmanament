
import os
import cloudinary
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

app.config['MAIL_SENDGRID_API_KEY'] = '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'
mail = MailSendGrid(app)