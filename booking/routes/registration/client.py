# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import current_user
# Import models
from booking.models.forms.client import ClientForm
from booking.models.clients import Client
from booking.models.users import User
# Import database
from booking.models.bases import db

@app.route('/register/client/', methods=['GET', 'POST'])
@app.route('/register/client/<int:business_id>/<string:business_referral>/', methods=['GET', 'POST'])
def register_client(business_id=1, business_referral=""):
    if business_id == 1:
        business_id = current_user.business.id
    form = ClientForm(request.form)
    if form.validate_on_submit():
        if Client.query.filter_by(business_id=business_id).filter_by(email=form.email.data).first() is None:
            client = Client(form.email.data, business_id, form.name.data, form.phone.data)
            db.session.add(client)
            db.session.commit()
            return redirect(url_for('clients'))
        else:
            flash("Client already exists with that email.", "error")
    return render_template("registration/client.html", form=form)

