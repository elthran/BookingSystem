from booking.models.bases import Base, db
from datetime import datetime


class Service(Base):
    name = db.Column(db.String(128), nullable=False)
    availability = db.Column(db.DateTime)

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    def __init__(self, name, business_id):
        self.name = name
        self.business_id = business_id
        self.availability = datetime.now()

    def __repr__(self):
        return '<Service %r (%r)>' % (self.name, self.id)

