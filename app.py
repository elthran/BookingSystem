from flask import Flask, render_template, request, redirect, url_for
from users import User

app = Flask(__name__)

users = [User()] # THIS SHOULD BE STORED IN THE DATABASE AND NOT BE HERE

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users.append(User(request.form["username"].title())) # SHOULD BE ADDING TO THE DATABASE
    return render_template('home.html', title="Login", users=users)

if __name__ == '__main__':
    app.run(debug=True)