from booking.models.bases import Base, db

class Service(Base):
    name = db.Column(db.String(128), nullable=False)

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    def __init__(self, name, business_id):
        self.name = name
        self.business_id = business_id

    def __repr__(self):
        return '<Service %r (%r)>' % (self.name, self.id)

