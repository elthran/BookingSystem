from booking.models.bases import Base, db
from werkzeug import generate_password_hash

class UserShell(Base):
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(192))
    # Business associated with the user
    business_id = db.Column(db.Integer)

    def __init__(self, name, email, business_id):
        self.name = name
        self.email = email
        self.password = None
        self.business_id = business_id

    def check_if_exists(self):
        # Put this function here or in the route?
        pass

    def __repr__(self):
        return '<User Shell %r (%r)>' % (self.email, self.id)
