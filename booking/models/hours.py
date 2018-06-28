from booking.models.bases import Base, db


class Hour(Base):
    """
    Here you can set the opening hours of any location. So you could set location 5 to be open from 9am-3pm on Monday and 1pm-6pm on Friday.
    Each interval of time would be its own object.
    """
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    day = db.Column(db.Integer)  # Which day of the week
    start = db.Column(db.Integer)  # What hour your availability starts
    length = db.Column(db.Integer)  # How many minutes you are available for

    def __init__(self, location_id, day, start_time, length):
        self.location_id = location_id
        self.day = day
        self.start = start_time
        self.length = length

    @property
    def end(self):
        return self.start + self.length

    def __repr__(self):
        return '<Business Hours: %r:00-%r:00 (%r)>' % (self.monday_open, self.monday_close, self.id)
