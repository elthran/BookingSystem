# Import flask dependencies
from flask import request, render_template, flash, redirect, url_for
# Import session handling
from flask_login import login_user
# Import the app itself
from booking import app
# Import models
from booking.models import User
# Import forms
from booking.models.forms.login import LoginForm

# Set the route and accepted methods
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # If sign in form is submitted
    form = LoginForm(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Welcome %s' % user.name, 'notice')
            return redirect(url_for('business_profile', chosen_year=2018, chosen_month=6, chosen_day=0))
        flash('Wrong email or password', 'error')

    return render_template("authentication/login.html", form=form)
