from booking.models.bases import Base, db


class Location(Base):
    # Needs to list all services offered here

    hours_id = db.Column(db.Integer, db.ForeignKey('hours.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # Your location information
    address = db.Column(db.String(128))
    town = db.Column(db.String(128))
    province = db.Column(db.String(128))
    country = db.Column(db.String(128))
    timezone = db.Column(db.String(128))
    postalcode = db.Column(db.String(128))

    def __init__(self, business_id):
        self.business_id = business_id
        self.hours_id = None
        self.address = None
        self.town = None
        self.province = None
        self.country = None
        self.timezone = None
        self.postalcode = None

    def __repr__(self):
        return '<Location %r (%r)>' % (self.email, self.id)
