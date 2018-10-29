# Import the app itself
from booking import app, db
# Import flask dependencies
from flask import render_template


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("index/about.html")
