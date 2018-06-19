from booking.models.bases import Base, db


class UserShell(Base):
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(192))
    # Business associated with the user
    business_id = db.Column(db.Integer)
    is_owner = db.Column(db.Boolean)

    def __init__(self, name, email, business_id, is_owner=False):
        self.name = name
        self.email = email
        self.password = None
        self.business_id = business_id
        self.is_owner = is_owner

    def check_if_exists(self):
        # Put this function here or in the route?
        pass

    def __repr__(self):
        return '<User Shell %r (%r)>' % (self.email, self.id)
