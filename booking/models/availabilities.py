from booking.models.bases import Base, db


class Availability(Base):
    # Needs to list all services offered here
    employee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    day = db.Column(db.Integer) # Which day of the week
    start = db.Column(db.Integer) # What hour your availability starts
    length = db.Column(db.Integer) # How many minutes you are available for

    def __init__(self, employee_id, day, start_time, length):
        self.employee_id = employee_id
        self.day = day
        self.start = start_time
        self.length = length

    @property
    def end(self):
        return self.start + self.length

    def __repr__(self):
        days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return '<(%r) %r:00-%r:00>' % (days[self.day], self.start, self.start + self.length)
