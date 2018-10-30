from booking.models.bases import Base, db


class Hour(Base):
    """
    Here you can set the opening hours of any location.
    So you could set location 5 to be open from 9am-3pm on Monday and 1pm-6pm on Friday.
    Each interval of time would be its own object.
    """
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    day = db.Column(db.Integer)  # Which day of the week
    start = db.Column(db.Integer)  # What hour your availability starts
    length = db.Column(db.Integer)  # How many minutes you are available for

    closed = db.Column(db.Boolean)  # If your store is closed that day

    def __init__(self, location_id, day, start_time, length, closed=False):
        self.location_id = location_id
        self.day = day
        self.start = start_time
        self.length = length
        self.closed = closed

    @property
    def end(self):
        return self.start + self.length

    def display(self, day, closed):
        days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if not closed:
            return '%r %r:00-%r:00' % (days[day], self.start, self.end)
        else:
            return '%r: Closed' % (days[day])

    def __repr__(self):
        return '%r:00-%r:00' % (self.start, self.end)
