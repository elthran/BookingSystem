# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
# Import models
from booking.models import User
# Import forms
from booking.models.forms.register import RegisterForm
# Import database
from booking.models.bases import db

@app.route('/register/<int:user_id>', methods=['GET', 'POST'])
def register(user_id):
    form = RegisterForm(request.form)
    user = User.query.filter_by(id=user_id).first()
    print(user)
    if form.validate_on_submit():
        user = User(form.email.data, form.password.data, 1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("authentication/register.html", form=form)