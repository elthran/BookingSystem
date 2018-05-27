from flask import request, render_template

from booking import app, users
from users import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users.append(User(request.form["username"].title())) # SHOULD BE ADDING TO THE DATABASE
    return render_template('home.html', title="Login", users=users)