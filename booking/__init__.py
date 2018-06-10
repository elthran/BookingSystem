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

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('private_config')

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
    return render_template('404.html'), 404

import booking.routes.authentication.main
import booking.routes.authentication.create_password
import booking.routes.authentication.register_new
import booking.routes.authentication.register_employee
import booking.routes.authentication.login
import booking.routes.authentication.logout
import booking.routes.bookings.book_appointment
import booking.routes.home

# Build the database:
# This will create the database file using SQLAlchemy
#db.drop_all()
db.create_all()

# This will handle user requests
from flask_login import LoginManager

from booking.models.users import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "signin"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()