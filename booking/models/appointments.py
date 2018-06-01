from booking.models.bases import Base, db


class Appointment(Base):
    # The business for which the appointment is for
    #business_id = db.Column(db.SmallInteger, db.ForeignKey('business.id'), nullable=False)

    # The length of the appointment in minutes
    length = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, business_id, length=60):
        self.business_id = business_id
        self.length = length

    def __repr__(self):
        return '<Appointment for business %r (ID: %r)>' % (self.business_id, self.id)
