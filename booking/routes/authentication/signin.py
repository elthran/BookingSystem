# Import flask dependencies
from flask import request, render_template, \
                  flash, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash

# Import the database object from the main app module

# Import module forms
from booking.models.forms.login import LoginForm

# Import module models (i.e. User)
from booking.models import User, Appointment

from booking import app

from booking.models.bases import db

# Set the route and accepted methods
@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    current_user = User("hey", "hey", "hey")
    db.session.add(current_user)
    current_user2 = User("hey2", "hey2", "hey")
    db.session.add(current_user2)
    print("All users:",User.query.all())
    print("All appointments:",Appointment.query.all())
    print("Current user:",current_user)

    # This deletes database but crashes the game: db.drop_all()
    # To query a user: current_user = User.query.first()
    # To delete all appointments and find out how many were deleted: number = Appointment.query.delete()
    # To save the database: db.session.commit()

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