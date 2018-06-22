# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required


@app.route('/client/list/', methods=['GET', 'POST'])
@app.route('/client/list/<int:business_id>/', methods=['GET', 'POST'])
@login_required
def client_list(business_id=1):
    return render_template("client/home.html")
