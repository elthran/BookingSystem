# Import flask dependencies
from flask import request, render_template, flash, redirect, url_for
# Import session handling
from flask_login import login_user
# Import the app itself
from booking import app, db
# Import models
from booking.models import User
# Import forms
from booking.models.analytics import AuthenticationEvent, UnvalidatedEvent
from booking.models.forms.login import LoginForm

from booking.models.bases import db


# Set the route and accepted methods
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # If sign in form is submitted
    form = LoginForm(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            if user.is_verified:
                login_user(user)
                login_event = AuthenticationEvent(user_id=user.id, activity="login")
                if login_event.validity:
                    db.session.add(login_event)
                else:
                    invalid_event = UnvalidatedEvent(table="authentication")
                    db.session.add(invalid_event)
                db.session.commit()
                return redirect(url_for('business_calendar', year=2018, month=6, day=0))
            else:
                return render_template("registration/verification.html", form=form, new=False)
    return render_template("index/login.html", form=form)
