from flask import Flask
from users import User

app = Flask(__name__)
app.config.from_object('private_config')

users = [User()] # THIS SHOULD BE STORED IN THE DATABASE AND NOT BE HERE

# noinspection PyUnresolvedReferences
import routes
