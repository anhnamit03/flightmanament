import math
import cloudinary.uploader
import flask
import flask_login
from flask import render_template, request, redirect, url_for, session, jsonify
from flask_login import login_required, current_user, login_user

from FlightManament import app, login_manager
import os
import stripe

from FlightManament.models import User


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bookticket")
def book_ticket():
    return render_template("bookticket.html")


@app.route("/sale")
def sale():
    return render_template("sale.html")


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
