# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('private_config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

import booking.routes.authentication.main
import booking.routes.authentication.password
import booking.routes.authentication.register
import booking.routes.authentication.login
import booking.routes.authentication.logout
import booking.routes.home

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

# This will handle user requests
from flask_login import LoginManager

from booking.models.users import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "signin"

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter(User.id==user_id).first()
    if user:
        return user
    else:
        return None