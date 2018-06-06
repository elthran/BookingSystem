# Import flask dependencies
from flask import flash, redirect, url_for
# Import session handling
from flask_login import logout_user
# Import the app itself
from booking import app
# Set the route and accepted methods
@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('Logout was successful')
    print("Logged out")
    return redirect(url_for('main'))
