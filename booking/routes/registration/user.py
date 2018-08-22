# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import login_user
# Import models
from booking.models.forms.user import UserForm
from booking.models.users import User
from booking.models.emails import VerifyEmail
# Import database
from booking.models.bases import db
import smtplib # For emailing

@app.route('/register/user/', methods=['GET', 'POST'])
@app.route('/register/user/<int:business_id>/<string:business_referral>/', methods=['GET', 'POST'])
def register_user(business_id=1, business_referral=""):
    if business_id == 1:
        owner = True
    else:
        owner = False
    form = UserForm(request.form)
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() is None:
            user = User(form.name.data, form.email.data, form.password.data, business_id, owner)
            db.session.add(user)
            db.session.commit()
            login_user(user)

            gmail_user = 'jachang4@gmail.com'
            gmail_password = 'Melissa4'
            sent_from = gmail_user
            to = [user.email]
            email_text = "Verify with:" + str(user.get_verification_link())
            print(email_text)
            print(to)
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.quit()
                print("Email sent")
            except:
                print('Email not sent...')

            if owner:
                return redirect(url_for('register_business'))
            else:
                return redirect(url_for('business_calendar'))
        else:
            flash("User already exists with that email.", "error")
    return render_template("index/sign_up.html", form=form, owner=owner)
