# Import the app itself
from booking import app, db
# Import flask dependencies
from flask import render_template


@app.route('/about', methods=['GET', 'POST'])
def about():
    print("Visiting the About page will reset the database.")
    # Build the tables in database, if the database exists.
    # Otherwise build using mysql: CREATE DATABASE IF NOT EXISTS booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    # This will create the database file using SQLAlchemy
    db.drop_all()  # no longer needed, try `python3 run.py -d`
    db.create_all()
    return render_template("index/about.html")
