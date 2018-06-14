# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect
# Import session management
from flask_login import login_required
# Import models
from booking.models.clients import Client
from booking import ALLOWED_EXTENSIONS, secure_filename
import os

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_required
@app.route('/profile/client/<int:business_id>/<int:client_id>/', methods=['GET', 'POST'])
def client_profile(business_id, client_id):
    client = Client.query.filter_by(business_id=business_id).filter_by(id=client_id).first()
    # Statement below is to allow users to upload files and attach to the client profile
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(str(client.business_id) + "-" + str(client.id) + "-1")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    client_uploads = []
    for filename in os.listdir('booking/static/uploads'):
        if filename[0] == str(client.business_id) and filename[2] == str(client.id):
            client_uploads.append(os.path.join('/static/uploads', filename))
    return render_template("profiles/client.html", client=client, client_uploads=client_uploads)
