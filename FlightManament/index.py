import math
import cloudinary.uploader
import flask
import flask_login
import stripe
import utils
import requests
from flask import render_template, request, redirect, url_for, session, jsonify

from flask_login import login_required, current_user, login_user

from FlightManament import app, mail, login_manager, stripe_keys

from FlightManament import app
from utils import *
from flask_mail import Message
from FlightManament.models import User

stripe.api_key = stripe_keys["secret_key"]


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/bookticket", methods=['get', 'post'])
def book_ticket():
    destinations = utils.get_name_airport()
    if request.method.__eq__("GET"):
        destination = request.args.get('destination')
        departure = request.args.get('departure')
        go_date = request.args.get('go_date')


    return render_template("bookticket.html",
                           destinations=destinations,
                           destination=destination,
                           departure=departure,
                           go_date=go_date,

                           )


@app.route("/introduce")
def introduce():
    return render_template("introduce.html")


@app.route("/sale")
def sale():
    return render_template("sale.html")


# login with sso
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
    user_info_url = 'https://www.googleapis.com/oauth2/v3/userinfo'

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
    user_info = session.get('user_info')
    user_name = ""

    # login wwith sso
    google_client_id = '1055243236583-dol1antfv33cudplah7tjb56787vefhg.apps.googleusercontent.com'
    redirect_uri = 'http://localhost:5000/callback_login_sso'
    auth_url = f'https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={google_client_id}&redirect_uri={redirect_uri}&scope=https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/contacts.readonly&access_type=online'

    if user_info is not None:
        # Check if 'names' field is present and not empty
        if 'name' in user_info and user_info['name']:
            # Use the first name from the list (you may adapt this based on your needs)
            user_name = user_info['name']
    error_msg = ""
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = utils.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect(url_for('home'))
        else:
            error_msg = "Tài khoản hoặc mật khẩu không chính xác"

    return render_template("login.html", error_msg=error_msg, user_name=user_name, auth_url=auth_url)


@app.route("/login_customer", methods=["GET", "POST"])
def login_customer():
    name = ""
    error_msg = ""
    if request.method == "POST":
        cccd = request.form.get('cccd')
        customer = utils.check_login_customer(cccd)
        if customer:
            login_user(customer=customer)
            return redirect(url_for('home'))
        else:
            error_msg = "Bạn chưa sử dụng dịch vụ của chúng tôi"

    return render_template("logincustomer.html", error_msg=error_msg)


@login_manager.user_loader
def load_user(user_id):
        if utils.get_user_by_id(user_id=user_id):
            return utils.get_user_by_id(user_id=user_id)
        else:
            return utils.get_customer_by_id(user_id=user_id)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect('login')


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


@app.route('/protected')
@login_required
def protected():
    print("current_user", current_user)
    return 'Logged in as: ' + current_user.name


@app.route('/test')
def test():
    return render_template('test.html')


@app.route("/401")
def ffgdd():
    return render_template('401.html')


@app.route("/payment")
def payment():
    return render_template('payment.html')


@app.route("/create-checkout-session", methods=['GET', 'POST'])
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Retrieve the product details from the form or database
        products = ['Product A', 'Product B', 'Product C']  # Replace this with your list of products
        amount = 1000000  # Set the amount in the smallest unit of your currency (e.g., cents for USD)

        # Create a PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='vnd',
            payment_method_types=["card"],
            payment_method_data={
                'type': 'card',
                'card[token]': request.form['stripeToken']
            },
            confirmation_method='manual',  # Use manual confirmation for better control
            confirm=True,  # Confirm the payment immediately,

        )
        return jsonify({'clientSecret': intent.client_secret})


        # checkout_session = stripe.checkout.Session.create(
        #     success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
        #     cancel_url=domain_url + "cancelled",
        #     payment_method_types=["card"],
        #     mode="payment",
        #     line_items=[
        #         {
        #             'price': 'price_1OHTpxAKLdt3jKp1W0zFWNKi',  # Sử dụng `price` ID của sản phẩm đã có sẵn
        #             'quantity': 1,
        #         }
        #     ]
        # )
        return jsonify({"sessionId": charge["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")


def handle_checkout_session(session):
    print("Payment was successful.")
    # TODO: run some custom code here


@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)


if __name__ == "__main__":
    app.run(debug=True)
