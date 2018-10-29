from booking.models.bases import Base, db


class Location(Base):
    # Needs to list all services offered here

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    users = db.relationship('User', backref='location')

    # Availabilities that the location has. This is tied to an employee
    availabilities = db.relationship('Availability', backref='location')
    # The opening hours of the location
    hours = db.relationship('Hour', backref='location')

    name = db.Column(db.String(128))

    # Your location information
    country = db.Column(db.String(128))
    province = db.Column(db.String(128))
    city = db.Column(db.String(128))
    address = db.Column(db.String(128))

    timezone = db.Column(db.String(128))
    postalcode = db.Column(db.String(128))

    email = db.Column(db.String(64))
    phone = db.Column(db.String(64))

    def __init__(self, business_id, name="Burnaby", email=None, phone=None):
        self.business_id = business_id
        self.name = name
        self.country = None
        self.province = None
        self.city = None
        self.address = None
        self.timezone = None
        self.postalcode = None

        self.mail = email
        self.phone = phone

    def get_employee_count(self):
        return len(self.users)

    def get_hours_by_day(self, day):
        return [hour for hour in self.hours if hour.day == day]

    def __repr__(self):
        return '<Location (%r)>' % (self.id)
