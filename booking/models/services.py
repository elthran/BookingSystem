from booking.models.bases import Base, db
from datetime import datetime


class Service(Base):
    name = db.Column(db.String(128), nullable=False)
    availability = db.Column(db.DateTime)
    cost = db.Column(db.Integer)
    length = db.Column(db.Integer)
    deposit_required = db.Column(db.Boolean)

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    # Needs to connect to all locations this ervice is offered at

    def __init__(self, name, business_id, price=0, length=30):
        self.name = name
        self.business_id = business_id
        self.availability = datetime.now()
        self.price = price
        self.length = length
        self.deposit_required = False

    def __repr__(self):
        return '<Service %r (%r)>' % (self.name, self.id)

