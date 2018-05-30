from flask import url_for
from werkzeug.utils import redirect

from booking import app


@app.route('/')
def home():
    return redirect(url_for('login'))