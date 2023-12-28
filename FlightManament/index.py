import math
import cloudinary.uploader
from flask import render_template, request, redirect, url_for, session, jsonify
from FlightManament import app
from utils import *
import os
import stripe


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/bookticket")
def book_ticket():
    return render_template("bookticket.html")


@app.route("/sale")
def sale():
    return render_template("sale.html")

# @app.route("/register", methods=['get', 'post'])
# def user_register():
#     err_mgs = ""
#     if request.method.__eq__('POST'):
#         name = request.form.get('name')
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         confirm = request.form.get('confirm')
#         avatar_path = None
#
#         try:
#             if password.strip().__eq__(confirm.strip()):
#                 avtar = request.files.get('avatar')
#                 if avtar:
#                     res = cloudinary.uploader.upload(avtar)
#                     avatar_path = res['secure_url']
#
#                 utils.add_user(name=name,
#                                username=username,
#                                password=password,
#                                email=email,
#                                avatar=avatar_path)
#                 return redirect(url_for('user_signin'))
#             else:
#                 err_mgs = "Mat khau khong khop!!!"
#         except Exception as ex:
#             err_mgs = "he thong dang co loi: " + str(ex)
#
#     return render_template("register.html", err_mgs=err_mgs)
#
#
# @app.context_processor
# def comon_response():
#     return {
#         'categories': utils.load_categories()
#     }
#
#
# @app.route('/user_login', methods=['get', 'post'])
# def user_signin():
#     err_mgs = ''
#     if request.method.__eq__('POST'):
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         user = utils.check_login(username, password)
#         if user:
#             login_user(user=user)
#             return  redirect(url_for('home'))
#         else:
#             err_mgs = 'username or password is incorrect'
#
#     return render_template('login.html', err_mgs=err_mgs)
#
#
# @app.route('/user_logout')
# def user_signout():
#     logout_user()
#     return redirect(url_for('user_signin'))
#
#
# @login.user_loader
# def user_load(user_id):
#     return utils.get_user_by_id(user_id)


if __name__ == "__main__":
    app.run(debug=True)