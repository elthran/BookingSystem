# Import flask dependencies
from flask import request, render_template, flash, session, redirect, url_for
# Import the app itself
from booking import app
# Used to create appointments. Might be moved somewhere else soon.
from datetime import datetime
# Import database
from booking.models.bases import db
# Import models
from booking.models import User
# Import forms
from booking.models.forms.login import LoginForm


# Set the route and accepted methods
@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    # If sign in form is submitted
    form = LoginForm(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
                session['user_id'] = user.id
                flash('Welcome %s' % user.email)
                return redirect(url_for('home'))
        flash('Wrong email or password', 'error-message')

    return render_template("authentication/signin.html", form=form)
