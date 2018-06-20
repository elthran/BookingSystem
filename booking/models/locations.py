from booking.models.bases import Base, db


class Location(Base):
    # Needs to list all services offered here

    hours_id = db.Column(db.Integer, db.ForeignKey('hours.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    name = db.Column(db.String(128))

    # Your location information
    address = db.Column(db.String(128))
    town = db.Column(db.String(128))
    province = db.Column(db.String(128))
    country = db.Column(db.String(128))
    timezone = db.Column(db.String(128))
    postalcode = db.Column(db.String(128))

    def __init__(self, hours_id, business_id, name="Burnaby", address=None, town=None):
        self.business_id = business_id
        self.hours_id = hours_id
        self.name = name
        self.address = address
        self.town = town
        self.province = None
        self.country = None
        self.timezone = None
        self.postalcode = None

    def __repr__(self):
        return '<Location (%r)>' % (self.id)
