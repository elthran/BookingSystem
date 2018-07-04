# Import the app itself
from booking import app
from flask import render_template, flash, jsonify, request
from flask_json import as_json
from flask_wtf import FlaskForm
from random import randint


@app.route('/json')
def json():
    return render_template('json.html')


@app.route('/handle_ajax_request', methods=["GET", "POST"])
@as_json
def background_process_test():
    number = randint(0, 10)
    message = "Python generated this random number for you: %r" % number
    print(message)
    return dict(data=number)
    # return jsonify(data=number)
