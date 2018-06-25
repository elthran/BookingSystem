# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required


@app.route('/business/clients/', methods=['GET', 'POST'])
@app.route('/business/clients/<int:business_id>/', methods=['GET', 'POST'])
@login_required
def clients(business_id=1):
    return render_template("business/clients.html")
