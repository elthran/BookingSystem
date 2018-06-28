# Import flask dependencies
from flask import render_template, request
# Import session management
from flask_login import login_required, current_user

# Import the app itself
from booking import app
from booking.models.forms.client import ClientSearchForm
from booking.functions.search import search_clients


@app.route('/business/clients/', methods=['GET', 'POST'])
@app.route('/business/clients/<int:business_id>/', methods=['GET', 'POST'])
@login_required
def clients(business_id=1):
    form = ClientSearchForm(request.form)
    viewable_clients = None
    if form.validate_on_submit():  # Currently
        viewable_clients = search_clients(form.keywords.data, current_user.business.id)
    else:  # Probably should show most 10 recent clients?
        viewable_clients = current_user.business.get_clients()
    return render_template("business/clients.html", clients=viewable_clients, form=form)
