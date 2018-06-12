# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for, flash
# Import models
from booking.models.users_shell import UserShell
from booking.models.users import User
from booking.models.businesses import Business
# Import forms
from booking.models.forms.register import EmployeeForm
# Import database
from booking.models.bases import db

@app.route('/register_employee/<int:business_id>', methods=['GET', 'POST'])
def register_employee(business_id):
    business = Business.query.filter_by(id=business_id).first()
    form = EmployeeForm(request.form)
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() is None:
            temporary_user = UserShell(form.name.data, form.email.data, business_id)
            db.session.add(temporary_user)
            db.session.commit()
            return redirect(url_for('create_password', user_id=temporary_user.id, business_id=business_id))
        flash("Email already exists in database", "error")
    return render_template("authentication/new_employee.html", form=form, business=business)