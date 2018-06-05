# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
# Import models
from booking.models import User
# Import forms
from booking.models.forms.register import PasswordForm
# Import database
from booking.models.bases import db

@app.route('/create_password/<string:name>/<string:business>/<string:email>', methods=['GET', 'POST'])
def create_password(name, business, email):
    form = PasswordForm(request.form)
    print("Creating user at email:", email)
    if form.validate_on_submit():
        print("Validating form")
        password = form.password.data
        user = User(name, email, password, business)
        db.session.add(user)
        db.session.commit()
        user_id = User.query.filter_by(email=user.email).first().id
        print("User id is:", user_id)
        return redirect(url_for('register', user_id=user_id))
    return render_template("authentication/password.html", form=form)