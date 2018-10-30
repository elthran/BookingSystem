from booking.models.bases import Base, db
from datetime import time


class Availability(Base):
    """
    Here you can set each availability that any employee has. Each availability is tied to an employee
    and it is also tied to a location. So for example, you could add an availability of employee 3 at location 2,
    from 9:00-5:00 on Tuesday.
    """
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    day = db.Column(db.Integer)  # Which day of the week
    start = db.Column(db.Time, nullable=False)  # What time your availability starts
    length = db.Column(db.Integer)  # How many minutes you are available for

    def __init__(self, location_id, user_id, day, hour, minute, length):
        self.location_id = location_id
        self.user_id = user_id
        self.day = day
        self.start = time(hour, minute, 0)
        self.length = length

    @property
    def end(self):
        """
        Returns a new time using the starting time but increasing the minutes by the session length
        """
        hours = self.length // 60
        minutes = self.length % 60
        return time(self.start.hour + hours, self.start.minute + minutes)

    def __repr__(self):
        days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return '(%r) %r-%r' % (days[self.day], self.start.strftime("%H:%M %Z"), self.end.strftime("%H:%M %Z"))
