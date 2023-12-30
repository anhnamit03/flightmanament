import math
import cloudinary.uploader
import flask
import flask_login
import stripe
import requests
from flask import render_template, request, redirect, url_for, session, jsonify

from flask_login import login_required, current_user, login_user

import FlightManament
from FlightManament import app, mail, login_manager

from FlightManament import app
from utils import *
from flask_mail import Message
from FlightManament.models import User



@app.route('/', methods=['GET', 'POST'])
def home():
    user_info = session.get('user_info')
    user_name =""

    # login wwith sso
    google_client_id = '1055243236583-dol1antfv33cudplah7tjb56787vefhg.apps.googleusercontent.com'
    redirect_uri = 'http://localhost:5000/callback_login_sso'
    auth_url = f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={google_client_id}&redirect_uri={redirect_uri}&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/contacts.readonly&access_type=online'

    if user_info is not None:
        # Check if 'names' field is present and not empty
        if 'name' in user_info and user_info['name']:
            # Use the first name from the list (you may adapt this based on your needs)
            user_name = user_info['name']

    return render_template("index.html", user_name=user_name, auth_url = auth_url)


@app.route("/bookticket", methods = ['get', 'post'])
def book_ticket():
    if request.method.__eq__('POST'):
        destination = request.form.get('destination')
        departure = request.form.get('departure')
        go_date = request.form.get('go_date')

    destinations = ["opt1", "opt2", "opt3", "opt4"]
    return render_template("bookticket.html", destinations = destinations)


@app.route("/introduce")
def introduce():
    return render_template("introduce.html")


@app.route("/sale")
def sale():
    return render_template("sale.html")


#login with sso
@app.route('/login_sso')
def login_sso():
    google_client_id = '1055243236583-dol1antfv33cudplah7tjb56787vefhg.apps.googleusercontent.com'
    redirect_uri = 'http://localhost:5000/callback_login_sso'
    auth_url = f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={google_client_id}&redirect_uri={redirect_uri}&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/contacts.readonly&access_type=online'

    return f'<a href="{auth_url}">Login with Google</a>'

@app.route('/log_out')
def log_out():
    session['user_info'] = None
    return redirect(url_for('home'))


@app.route('/callback_login_sso')
def callback_login_sso():
    code = request.args.get('code')
    google_client_id = '1055243236583-dol1antfv33cudplah7tjb56787vefhg.apps.googleusercontent.com'
    google_client_secret = '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'
    redirect_uri = 'http://localhost:5000/callback_login_sso'

    token_url = 'https://accounts.google.com/o/oauth2/token'
    token_data = {
        'code': code,
        'client_id': google_client_id,
        'client_secret': google_client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    # Get access token and user info
    response = requests.post(token_url, data=token_data)
    token_info = response.json()

    # Use the access token to get user info
    user_info_url =  'https://www.googleapis.com/oauth2/v3/userinfo'

    headers = {'Authorization': f'Bearer {token_info["access_token"]}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    # Store user info in session or database as needed
    session['user_info'] = user_info

    if user_info is not None:
        #  send message
        msg = Message("Hello",
                      sender="dangvykhoi@gmail.com",

                      recipients=[user_info["email"]])

        msg.template_id = 'd-3b20516cd9424fe59bed6499de841098'
        msg.dynamic_template_data = {'name': user_info["name"]}

    mail.send(msg)



    # // send otp
    return redirect(url_for('home'))


# end region


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                   <input type='text' name='username' id='username' placeholder='username'/>
                   <input type='password' name='password' id='password' placeholder='password'/>
                   <input type='submit' name='submit'/>
               </form>
           '''
    username = request.form['username']
    password = request.form['password']

    # Validate credentials (replace this with your actual validation logic)
    if username is not None and password is not None:
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'

@login_manager.user_loader
def load_user(user_id):
    print("user is", user_id)
    return User.query.filter_by(username=user_id).first()

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'



@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


@app.route('/protected')
@login_required
def protected():
    print("current_user",current_user)
    return 'Logged in as: ' + current_user.name

@app.route('/checkout', methods=['POST'])
def cteate_checkout_session():
    try:
        checkout_session = stripe.checkout.Sesion.create(
            line_items=[
                {
                    "price":"price_1OSXXuAKLdt3jKp1cjT0pjwe",
                    "quantity":1
                }
            ],
            mode = "subscription"


        )
    except Exception as e:
        return str(e)

    return redirect()


@app.route("/hello")
def hello_world():
    return jsonify("hello, world!")


@app.route("/")
def index1():
    return render_template("index1.html")

# @app.route("/config")
# def get_publishable_key():
#     stripe_config = {"publicKey": stripe_keys["publishable_key"]}
#     return jsonify(stripe_config)

if __name__ == "__main__":
    app.run(debug=True)
