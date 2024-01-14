import cloudinary.uploader
import flask_login
import stripe
import utils
import requests
from flask import render_template, request, redirect, url_for, session, jsonify, Response
from flask_login import login_required, current_user, login_user
from FlightManament import  mail, login_manager, stripe_keys
from utils import *
from FlightManament import app

from flask_mail import Message
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



    # check user already in db
    user = utils.check_login_by_email(user_info["email"])
    if user:
        login_user(user=user)
        return redirect(url_for('home'))


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


@app.route('/test', methods=['get', 'post'])
def test():
    selected_flight_id = session.get('selected_flight_id')
    flight_info = utils.reder_interface_for_book_ticket_customer(selected_flight_id)
    value_from_session = session.get('list_seat')
    price = 0
    for item in value_from_session:
        if int(item) in flight_info.list_seat_rank_1:
            price += flight_info.price_seat_rank_1
        elif int(item) in flight_info.list_seat_rank_2:
            price += flight_info.price_seat_rank_2
    session["price"] = price
    a = type(flight_info.list_seat_rank_1)



    return render_template('test.html',value_from_session=value_from_session, flight_info=flight_info, a=a)


@app.route("/401")
def ffgdd():
    return render_template('401.html')


@app.route("/payment", methods=["GET", "POST"])
def payment():
    list_customers = []
    value_from_session = session.get('list_seat')
    if request.method.__eq__('POST'):
         for item in value_from_session:
             name = request.form.get('username' + item)
             CCCD = request.form.get('cccd' + item)
             gender = request.form.get('gender' + item)
             phone = request.form.get('phone' + item)
             email = request.form.get('email' + item)
             birthday = request.form.get('birthday' + item)
             customer = {'name': name,'CCCD': CCCD,'gender': gender,'phone': phone,'email': email,'birthday': birthday}
             list_customers.append(customer)
         session["list_customers"] = list_customers
    return render_template('payment.html')


@app.route("/create-checkout-session", methods=['GET', 'POST'])
def create_checkout_session():
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # get infor of customer payment
        name = request.form.get('name')
        identity_number = request.form.get('identityNumber')
        gender = request.form.get('gender')
        phone = request.form.get('numberPhone')
        email = request.form.get('email')
        birth_day = request.form.get('birthDay')
        amount = session.get('price')# Set the amount in the smallest unit of your currency (e.g., cents for USD)
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
        session["email_to"] = email
        session["name_to"] = name
        session["payment_state"] = True
        session["buyer"] = {'name': name,'CCCD': identity_number,'gender': gender,'phone': phone,'email': email,'birthday': birth_day}
        return jsonify({'clientSecret': intent.client_secret})
    except Exception as e:
        return jsonify(error=str(e))


@app.route("/success")
def success():
    # save data success

    # push noti

    if "payment_state" in session:

        buyer = session.get('buyer')
        if buyer:
            utils.add_customer(buyer['name'], buyer['CCCD'], int(buyer['gender']), buyer['phone'], buyer['email'], buyer['birthday'])
        list_customer = session.get('list_customers')
        if list_customer:
            for customer in list_customer:
                print(list_customer)
                utils.add_customer(customer['name'], customer['CCCD'], int(customer['gender']), customer['phone'], customer['email'], customer['birthday'])

        selected_flight_id = session.get('selected_flight_id')
        value_from_session = session.get('list_seat')
        for i in range(len(value_from_session)):


            utils.add_ticket(value_from_session[i],utils.get_id_customer(buyer['CCCD']),
                             utils.get_id_customer(list_customer[i]['CCCD']),
                             selected_flight_id,1)
        check_payment = session["payment_state"]
        if check_payment:
            # send mail
            email = session['email_to']
            name = session["name_to"]
            if email:
                #  send message
                msg = Message("Hello",
                              sender="dangvykhoi@gmail.com",
                              recipients=[email])
                msg.template_id = 'd-3b20516cd9424fe59bed6499de841098'
                msg.dynamic_template_data = {'name': name}
                mail.send(msg)
                return render_template("success.html")
    else:
        return redirect(url_for('home'))


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


@app.route("/hrmcheck", methods=['get', 'post'])
def hrmcheck():
    message1 = ""
    message2 = ""
    avatar_path = None
    list_role = utils.get_all_roles()
    team_flight = utils.get_all_team_flight()
    if request.method.__eq__('POST'):
        if request.form.get('action') == 'form1_submit':
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')
            phone = request.form.get('phone')
            name = request.form.get('fullname')
            birthday = request.form.get('birthday')
            CCCD = request.form.get('cccd')
            avatar = request.files.get('avata')
            if avatar:
                res = cloudinary.uploader.upload(avatar)
                avatar_path = res['secure_url']
            gender = request.form.get('gender').lower() == 'true'
            id_role = utils.get_id_role(request.form.get('role'))
            id_team_flight = request.form.get('team_flight')
            utils.add_user(username=username,
                    password=password,
                    avatar=avatar_path,
                    name=name,
                    CCCD=CCCD,
                    gender=gender,
                    phone=phone,
                    email=email,
                    birthday=birthday,
                    id_role=id_role,
                    id_team_flight=id_team_flight)
            message1 = "Đã thêm thành công 1 user"
        elif request.form.get('action') == 'form2_submit':
            teamflight = request.form.get('teamflight')
            utils.add_team_flight(teamflight)
            message2 = "Thêm thành công 1 team fly"
    return render_template("hr_manager.html",list_role=list_role, team_flight=team_flight,message1=message1,message2=message2)


@app.route('/flightmanager')
def flightmanager():
    all_flight = []  # Khởi tạo danh sách trống
    destinations = utils.get_name_airport()
    if request.method.__eq__("GET"):
        destination = request.args.get('destination')
        departure = request.args.get('departure')
        go_date = request.args.get('go_date')
        if destination and departure and go_date:
            list_flight_id = utils.get_flight(destination, departure, go_date)

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
    return render_template("flightmanager.html",
                           destinations=destinations,
                           destination=destination,
                           departure=departure,
                           go_date=go_date,
                           all_flight=all_flight,
                           )


if __name__ == "__main__":
    from FlightManament.admin import *
    app.run(debug=True)
