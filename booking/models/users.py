# Define a base model for other database tables to inherit
from booking.models.bases import Base, db


# Define a User model
class User(Base):

    # User Name
    name = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False,  unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password
        self.role = 0
        self.status = 0

    def __repr__(self):
        return '<User %r>' % (self.name)
