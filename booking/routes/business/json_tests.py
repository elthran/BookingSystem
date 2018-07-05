# Import the app itself
from booking import app
from flask import render_template, flash, jsonify, request
from flask_json import as_json
from flask_wtf import FlaskForm
from random import randint


@app.route('/json')
def json():
    return render_template('json.html')


@app.route('/handle_ajax_request', methods=["POST"])
@as_json
def background_process_test():
    # You don't need to parse the request.
    if request.is_json:
        data = request.get_json()
        print("Sent data:", repr(data))
    number = randint(0, 10)
    message = "Python generated this random number for you: %r" % number
    print(message)
    # can replace with return flask.jsonify() or a bunch of other options.
    return dict(data=number)
