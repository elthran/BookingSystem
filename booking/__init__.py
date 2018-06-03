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


import booking.routes.authentication.signin
import booking.routes.authentication.register
import booking.routes.home
import booking.routes.index

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
