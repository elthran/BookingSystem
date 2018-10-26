# Import flask dependencies
from flask import flash, redirect, url_for
# Import session handling
from flask_login import logout_user, current_user
# Import the app itself
# Set the route and accepted methods
from booking.models.analytics import AuthenticationEvent
from booking import app, db


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    print("User logging out")
    login_event = AuthenticationEvent(user_id=current_user.id, activity="logout")
    db.session.add(login_event)
    db.session.commit()
    logout_user()
    flash('Logout was successful')
    return redirect(url_for('home'))
