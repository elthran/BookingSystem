# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, flash, url_for
# Import models
from booking.models import User
# Import database
from booking.models.bases import db

@app.route('/verify/user/')
@app.route('/verify/user/<int:user_id>/<string:verification_link>/')
def verification(user_id=0, verification_link=""):
    user = User.query.filter_by(id=user_id).first()
    user.is_verified = True
    db.session.commit()
    flash("Account verified!")
    print("Account verified!")
    return redirect(url_for('business_calendar'))