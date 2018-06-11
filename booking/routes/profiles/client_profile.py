# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models.clients import Client

@login_required
@app.route('/profile/client/<int:business_id>/<int:client_id>/')
def client_profile(business_id, client_id):
    client = Client.query.filter_by(business_id=business_id).filter_by(id=client_id).first()
    print(client)
    return render_template("profiles/client_profile.html", client=client)