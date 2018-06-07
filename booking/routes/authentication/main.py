# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for, flash
# Import models
from booking.models.users_shell import UserShell
from booking.models.businesses_shell import BusinessShell
from booking.models.users import User
from booking.models.businesses import Business
# Import forms
from booking.models.forms.register import MainForm
# Import database
from booking.models.bases import db

@app.route('/', methods=['GET', 'POST'])
def main():
    users = User.query.all()
    businesses = Business.query.all()
    for user in users:
        print("Printing user::", user)
    for business in businesses:
        print("Printing business::", business)
    form = MainForm(request.form)
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() == None:
            temporary_business = BusinessShell(form.business.data)
            db.session.add(temporary_business)
            db.session.flush()
            temporary_user = UserShell(form.name.data, form.email.data, temporary_business.id)
            db.session.add(temporary_user)
            db.session.commit()
            return redirect(url_for('create_password', user_id=temporary_user.id, business_id=temporary_business.id))
        flash("Email already exists in database", "error")
    return render_template("authentication/main.html", form=form)
