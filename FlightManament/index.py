import math
import cloudinary.uploader
import flask
import flask_login
import requests
from flask import render_template, request, redirect, url_for, session, jsonify

from flask_login import login_required, current_user, login_user

from FlightManament import app, login_manager

from FlightManament import app
from utils import *

import os
import stripe

from FlightManament.models import User


@app.route('/', methods=['GET', 'POST'])
def home():
    user_info = session.get('user_info')
    user_name = ""
    if user_info:
        # Check if 'names' field is present and not empty
        if 'names' in user_info and user_info['names']:
            # Use the first name from the list (you may adapt this based on your needs)
            user_name = user_info['names'][0].get('displayName', 'Guest')


    return render_template("index.html", user_name=user_name)






@app.route("/bookticket")
def book_ticket():
    return render_template("bookticket.html")


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
    user_info_url = 'https://people.googleapis.com/v1/people/me?personFields=names'

    headers = {'Authorization': f'Bearer {token_info["access_token"]}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    # Store user info in session or database as needed
    session['user_info'] = user_info



    return redirect(url_for('home'))


# end region


@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    # Validate credentials (replace this with your actual validation logic)
    if username is not None and password is not None:

        user = User()
        user.id = username

        login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'

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


@login_manager.user_loader
def load_user(user_id):
    print("user is", user_id)
    return User.query.filter_by(username=user_id).first()


if __name__ == "__main__":
    app.run(debug=True)
