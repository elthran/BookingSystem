from booking.models.bases import Base, db

class Appointment(Base):
    # The business for which the appointment is for
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # The client for which the appointment is for
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    # The day and time of the appointment
    date = db.Column(db.DateTime, nullable=False)

    # The length of the appointment in minutes
    length = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, business_id, client_id, length, date):
        self.business_id = business_id
        self.client_id = client_id
        self.length = length
        self.date = date

    def __repr__(self):
        return '<Appointment (%r) is %r minutes long on %r/%r/%r at %r:%r>' % (self.id, self.length, self.date.year, self.date.month, self.date.day,
                                                            self.date.hour, self.date.minute)
