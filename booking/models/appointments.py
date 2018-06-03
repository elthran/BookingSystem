from booking.models.bases import Base, db

class Appointment(Base):
    # The business for which the appointment is for
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # The day and time of the appointment
    date = db.Column(db.DateTime, nullable=False)

    # The length of the appointment in minutes
    length = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, business_id, length, date):
        self.business_id = business_id
        self.length = length
        self.date = date

    def __repr__(self):
        return '<Appointment (%r) on %r/%r/%r at %r:%r>' % (self.id, self.date.year, self.date.month, self.date.day,
                                                            self.date.hour, self.date.minute)
