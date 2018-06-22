# Magical built-in function relating to sockets?
import socket

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# CSRF Protection
from flask_wtf.csrf import CSRFProtect

# Imports settings from the private security file
import private_config

UPLOAD_FOLDER = 'booking/static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Define the WSGI application object
app = Flask(__name__)

# Configurations (Klondikemarlen suggest moving the configs to the config file. Smart idea! Will implement)
app.config.from_object('private_config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Check location of code whether server or local
if 'liveweb' in socket.gethostname():  # Running on server (pythonanywhere)
    app.config['SQLALCHEMY_DATABASE_URI'] = private_config.SERVER_DATABASE_URI

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Ensbles CSRF protection
CSRFProtect(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    print("Error:", error)
    return render_template('404.html'), 404


import booking.routes.authentication.home
import booking.routes.authentication.login
import booking.routes.authentication.logout

import booking.routes.registration.business
import booking.routes.registration.user
import booking.routes.registration.client
import booking.routes.registration.verification

import booking.routes.bookings.appointment

import booking.routes.profiles.client
import booking.routes.profiles.employee
import booking.routes.profiles.appointment

import booking.routes.business.home

import booking.routes.client.home

# Build the database:
# This will create the database file using SQLAlchemy
# db.drop_all()  # no longer needed, try `python3 run.py -d`
db.create_all()

# This will handle user requests
from flask_login import LoginManager

from booking.models.users import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
