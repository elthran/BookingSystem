# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
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
        name = form.name.data
        business_name = form.business.data
        email = form.email.data
        temp_business = BusinessShell(business_name)
        db.session.add(temp_business)
        db.session.flush()
        business_id = temp_business.id
        temp_user = UserShell(name, email, business_id)
        db.session.add(temp_user)
        db.session.flush()
        user_id = temp_user.id
        db.session.commit()
        return redirect(url_for('create_password', user_id=user_id, business_id=business_id))
    return render_template("authentication/main.html", form=form)
