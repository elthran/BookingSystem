# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template


@app.route('/features', methods=['GET', 'POST'])
def features():
    return render_template("index/features.html")
