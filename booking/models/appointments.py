from booking.models.bases import Base, db
from datetime import timedelta


class Appointment(Base):
    # The business for which the appointment is for
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # The client for which the appointment is for
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    # The day and time of the appointment
    date = db.Column(db.DateTime, nullable=False)

    # The length of the appointment in minutes
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))

    # If the user has paid yet or not
    paid = db.Column(db.Boolean)

    # Name of practitioner, if chosen
    practitioner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, business_id, client_id, service_id, date, practitioner_id=None):
        self.business_id = business_id
        self.client_id = client_id
        self.service_id = service_id
        self.date = date
        self.practitioner_id = practitioner_id
        self.paid = False

    def get_end_time(self):
        return (self.date + timedelta(minutes=self.service.length)).time()

    def __repr__(self):
        return '<Appointment (%r) is on %r/%r/%r at %r:%r>' % (
            self.id, self.date.year, self.date.month, self.date.day,
            self.date.hour, self.date.minute)
