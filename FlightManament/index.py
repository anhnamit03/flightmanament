import math
import time
import pickle

import cloudinary.uploader
import flask
import flask_login
import stripe
import utils
import requests
from flask import render_template, request, redirect, url_for, session, jsonify, Response

from flask_login import login_required, current_user, login_user

from FlightManament import app, mail, login_manager, stripe_keys

from FlightManament import app
from utils import *
from flask_mail import Message
from FlightManament.models import User
import jwt

stripe.api_key = stripe_keys["secret_key"]


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/bookticket", methods=['get', 'post'])
def book_ticket():
    all_flight = []  # Khởi tạo danh sách trống
    destinations = utils.get_name_airport()
    if request.method.__eq__("GET"):
        destination = request.args.get('destination')
        departure = request.args.get('departure')
        go_date = request.args.get('go_date')
        if destination and departure and go_date:
            list_flight_id= utils.get_flight(destination, departure, go_date)

            if list_flight_id:
                for flight_id in list_flight_id:
                    flight_info = utils.reder_interface_for_book_ticket_customer(flight_id)
                    if flight_info:
                        all_flight.append(flight_info)
    list_seat = []
    if request.method.__eq__("POST"):
        session["list_seat"] = request.form.getlist('seat')
        session['selected_flight_id'] = request.form.get('id_flight')
        return redirect(url_for('test'))
    return render_template("bookticket.html",
                           destinations=destinations,
                           destination=destination,
                           departure=departure,
                           go_date=go_date,
                           all_flight=all_flight,
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

def verify_captcha_token(token):
    recaptcha_secret_key = '6LeVETMnAAAAALGi8Z7sSvQ9HM_GkMD7wQUU2ZLG'  # Replace with your actual secret key
    recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': recaptcha_secret_key,
        'response': token
    }
    response = requests.post(recaptcha_url, data=data)
    result = response.json()

    # Check the result from the captcha verification
    if result['success']:
        # Captcha verification successful, continue processing
        return True
    else:
        # Captcha verification failed, handle accordingly
        return False

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
        recaptcha_token = request.form.get('recaptchaToken')

        # // veryfy capcha
        if not recaptcha_token or not verify_captcha_token(recaptcha_token):
            return render_template('401.html')




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
    selected_flight_id = session.get('selected_flight_id')
    flight_info = utils.reder_interface_for_book_ticket_customer(selected_flight_id)
    value_from_session = session.get('list_seat')
    a =  type(flight_info.list_seat_rank_1)
    return render_template('test.html',value_from_session=value_from_session, flight_info=flight_info, a=a)


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


@app.route('/send_noti')
def index():
    return render_template('send_noti.html')


@app.route('/firebase-messaging-sw.js')
def firebase_messaging_sw():
    # Assuming 'firebase-messaging-sw.js' is in the 'static' folder
    with open('static/firebase-messaging-sw.js', 'r') as file:
        content = file.read()
    response = Response(content, content_type='application/javascript')
    return response


@app.route('/send_notification', methods=['POST'])
def send_notification():
    try:
        FCM_SERVER_KEY = 'AAAAsnOpY00:APA91bGP21V5yJ_tcs3ZiSy-zrAwSBth0DXW8UsMMU9vNLxJpx8PGc99FOJIm62rneze1Bu5o2KtSeehKZAZki8Xpky4n5Jcjc2K7xVn-PlVwaN56bDGRlt2EDNMKuxBnwrpcId4Zzbs'
        FCM_ENDPOINT = 'https://fcm.googleapis.com/fcm/send'
        # Get the FCM token from the request
        token = request.json.get('token')

        # Customize your notification payload
        notification_payload = {
            'to': token,
            'notification': {
                'title': 'Bạn đã đặt hàng thành công',
                'body': 'Bạn đã đặt hàng thành công vui lòng vào email để kiểm tra',
                'click_action': 'FLUTTER_NOTIFICATION_CLICK'  # Adjust as needed
            },
            'data': {
                'title': 'Bạn đã đặt hàng thành công',
                'body': 'Bạn đã đặt hàng thành công vui lòng vào email để kiểm tra',
                'icon': 'https://www.honda.com.vn/o-to/san-pham/honda-city/assets/imgs/message/bg_popup.jpg',
                'click_action': 'FLUTTER_NOTIFICATION_CLICK',

            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'key={FCM_SERVER_KEY}'
        }

        print('FCM Response:', token)

        response = requests.post(FCM_ENDPOINT, json=notification_payload, headers=headers)
        print('FCM Response:', response.text)

        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Notification sent successfully'})
        else:
            return jsonify({'success': False, 'message': 'Failed to send notification'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})



def handle_checkout_session(session):
    print("Payment was successful.")
    # TODO: run some custom code here


@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)


@app.route("/forme")
def forme():
    return render_template("forme.html")



@app.route("/hrmcheck")
def hrmcheck():
    list_role =  utils.get_all_roles()
    team_flight = utils.get_all_team_flight()
    return render_template("hr_manager.html",list_role=list_role, team_flight=team_flight)


if __name__ == "__main__":
    app.run(debug=True)
