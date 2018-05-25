from flask import Flask, render_template, request, redirect, url_for
from users import User

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form["username"]
        return render_template('home.html')
    return render_template('home.html', title="Login")

if __name__ == '__main__':
    app.run()