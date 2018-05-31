# Import flask dependencies
from flask import request, render_template, \
                  flash, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash

# Import the database object from the main app module

# Import module forms
from booking.models.forms.login import LoginForm

# Import module models (i.e. User)
from booking.models import User

from booking import app

# Set the route and accepted methods
@app.route('/signin/', methods=['GET', 'POST'])
def signin():

    print(User.query.all())

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('authentication.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("authentication/signin.html", form=form)
