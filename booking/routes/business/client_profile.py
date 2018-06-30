# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, flash
# Import session management
from flask_login import login_required
# Import models
from booking.models.clients import Client
from booking.functions.uploads import allowed_file, new_file_name, resize_image

import os
from PIL import Image

@login_required
@app.route('/business/client/<int:business_id>/<int:client_id>/', methods=['GET', 'POST'])
def client_profile(business_id, client_id):
    client = Client.query.filter_by(business_id=business_id).filter_by(id=client_id).first()
    # Statement below is to allow users to upload files and attach to the client profile
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash("No file chosen.", "error")
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash("Browser can't find file.", "error")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            upload = Image.open(file)   # Opens the uploaded file
            upload = resize_image(upload)   # Resizes the uploaded file
            filename = new_file_name(client, ".png")
            upload.save(filename, "PNG") # Saves the uploaded file
            flash("File uploaded successfully", "notice")
    client_uploads = []
    for filename in os.listdir('booking/static/uploads'):
        if filename[0] == str(client.business_id) and filename[2] == str(client.id):
            client_uploads.append(os.path.join('/static/uploads', filename))
    return render_template("business/client_profile.html", client=client, client_uploads=client_uploads)
