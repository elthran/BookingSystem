# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, url_for, redirect, flash
# Import session management
from flask_login import login_required
# Import calendar
from calendar import monthcalendar
from datetime import datetime
from booking.models.calendars import CustomCalendar
from booking import ALLOWED_EXTENSIONS, secure_filename
import os


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/business/home/', methods=['GET', 'POST'])
@app.route('/business/home/<int:year>/<int:month>/<int:day>', methods=['GET', 'POST'])
@login_required
def business_profile(year=datetime.now().year, month=datetime.now().month, day=0):
    custom_calendar = CustomCalendar(year, month, day)
    calendar_month = monthcalendar(year, month)
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    all_uploads = []
    for filename in os.listdir('booking/static/uploads'):
        all_uploads.append(os.path.join('/static/uploads', filename))
    return render_template("business/home.html", custom_calendar=custom_calendar, calendar_month=calendar_month, day=day, month=month, year=year, all_uploads=all_uploads)
