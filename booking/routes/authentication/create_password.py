# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
# Import models
from booking.models.users_shell import UserShell
# Import forms
from booking.models.forms.register import PasswordForm
# Import database
from booking.models.bases import db


@app.route('/create_password/<int:user_id>/<int:business_id>', methods=['GET', 'POST'])
def create_password(user_id, business_id):
    form = PasswordForm(request.form)
    user = UserShell.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        password = form.password.data
        user.password = password
        db.session.commit()
        return redirect(url_for('register_new', user_id=user_id, business_id=business_id))
    return render_template("authentication/password.html", form=form)
