from booking.models.bases import Base, db
from datetime import datetime


class Service(Base):
    name = db.Column(db.String(128), nullable=False)
    availability = db.Column(db.DateTime)
    cost = db.Column(db.Float(2))
    length = db.Column(db.Integer)
    deposit = db.Column(db.Boolean) # If a deposit is needed to book this
    location_id = db.Column(db.Integer) # Which location this is available at
    locations = db.Column(db.Boolean) # If this is true, it's available at every location at your business
    appointments = db.relationship('Appointment', backref='service')

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    # Needs to connect to all locations this service is offered at

    def __init__(self, name, business_id, cost, length):
        self.name = name
        self.business_id = business_id
        self.cost = cost
        self.length = length
        self.availability = datetime.now()
        self.deposit = False
        self.location_id = 1
        self.locations = False

    def get_description(self):
        return "%r for %r minutes - $%r" % (self.name, self.length, self.cost)

    def __repr__(self):
        return '%r for $%r and a length of %r min' % (self.name, self.cost, self.length)

