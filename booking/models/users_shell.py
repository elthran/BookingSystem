from booking.models.bases import Base, db
from werkzeug import generate_password_hash

class UserShell(Base):
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(192))
    # Business associated with the user
    business_id = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)

    def __init__(self, name, email, business_id, is_admin=False):
        self.name = name
        self.email = email
        self.password = None
        self.business_id = business_id
        self.is_admin = is_admin

    def check_if_exists(self):
        # Put this function here or in the route?
        pass

    def __repr__(self):
        return '<User Shell %r (%r)>' % (self.email, self.id)
