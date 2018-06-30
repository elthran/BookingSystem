# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request
# Import session handling
from flask_login import current_user
# Import models
from booking.models.forms.service import ServiceForm
from booking.models.services import Service
from booking.models.locations import Location
# Import database
from booking.models.bases import db

@app.route('/business/edit_service/<int:service_id>/', methods=['GET', 'POST'])
def edit_service(service_id):
    form = ServiceForm(request.form)
    service = Service.query.get(service_id)
    location = Location.query.filter_by(business_id=current_user.business.id).filter_by(id=1).first()
    if form.validate_on_submit():
        service.name = form.name.data
        service.cost = form.cost.data
        service.length = form.length.data
        db.session.commit()
        return redirect(url_for('business_service'))
    return render_template("business/edit_service.html", form=form, location=location, service=service)
