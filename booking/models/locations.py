from booking.models.bases import Base, db


class Location(Base):
    # Needs to list all services offered here

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # Availabilities that the location has. This is tied to an employee
    availabilities = db.relationship('Availability', backref='location')
    # The opening hours of the location
    hours = db.relationship('Hour', backref='location')

    name = db.Column(db.String(128))

    # Your location information
    address = db.Column(db.String(128))
    town = db.Column(db.String(128))
    province = db.Column(db.String(128))
    country = db.Column(db.String(128))
    timezone = db.Column(db.String(128))
    postalcode = db.Column(db.String(128))

    def __init__(self, business_id, name="Burnaby", address=None, town=None):
        self.business_id = business_id
        self.name = name
        self.address = address
        self.town = town
        self.province = None
        self.country = None
        self.timezone = None
        self.postalcode = None

    def get_hours_by_day(self, day):
        return [hour for hour in self.hours if hour.day == day]

    def __repr__(self):
        return '<Location (%r)>' % (self.id)
