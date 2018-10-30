# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
# Import session management
from flask_login import login_required, current_user
# Import models
from booking.models.clients import Client
from booking.models.forms.client import EditClientForm
# Import database
from booking.models.bases import db


@app.route('/business/edit_client/', methods=['GET', 'POST'])
@app.route('/business/edit_client/<int:client_id>/', methods=['GET', 'POST'])
@login_required
def edit_client(client_id):
    client = Client.query.get(client_id)
    form = EditClientForm(request.form)
    if form.validate_on_submit():
        client.name = form.name.data
        client.email = form.email.data
        client.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('client_profile', business_id=current_user.business.id, client_id=client.id))
    return render_template("business/edit_client.html", client=client, form=form)
