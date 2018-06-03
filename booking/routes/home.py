# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request
# Import models
from booking.models import User
# Import database
from booking.models.bases import db

@app.route('/home')
def home():
    users = User.query.all()
    print(users)
    return render_template("home.html", users=users)