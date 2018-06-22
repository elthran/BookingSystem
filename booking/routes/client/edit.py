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



@app.route('/client/edit/', methods=['GET', 'POST'])
@app.route('/client/edit/<int:client_id>/', methods=['GET', 'POST'])
@login_required
def client_edit(client_id):
    client = Client.query.filter_by(business_id=current_user.business.id).filter_by(id=client_id).first()
    form = EditClientForm(request.form)
    if form.validate_on_submit():
        client.name = form.name.data
        client.email = form.email.data
        client.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('client_profile', business_id=current_user.business.id, client_id=client.id))
    return render_template("client/edit.html", client=client, form=form)