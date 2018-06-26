# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import current_user
# Import models
from booking.models.forms.service import ServiceForm
from booking.models.services import Service
from booking.models.locations import Location
# Import database
from booking.models.bases import db

@app.route('/business/edit_service/<int:id>', methods=['GET', 'POST'])
def edit_service(id):
    form = ServiceForm(request.form)
    location = Location.query.filter_by(business_id=current_user.business.id).filter_by(id=1).first()
    if form.validate_on_submit():
        service = Service(form.name.data, current_user.business.id, form.cost.data, form.length.data)
        db.session.add(service)
        db.session.commit()
        return redirect(url_for('business_service'))
    return render_template("business/add_service.html", form=form, location=location)
