from booking.models.bases import Base, db


class User(Base):
    # User Name
    name = db.Column(db.String(128), nullable=False, unique=True)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r (ID %r)>' % (self.name, self.id)
