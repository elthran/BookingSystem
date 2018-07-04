# Import the app itself
from booking import app
from flask import render_template, flash
from random import randint


@app.route('/json')
def json():
    return render_template('json.html')


@app.route('/background_process_test')
def background_process_test():
    number = randint(0, 10)
    message = "Python generated this random number for you: %r" % number
    print(message)
    return str(number)
