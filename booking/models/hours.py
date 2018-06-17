from booking.models.bases import Base, db


class Hours(Base):
    # Needs to list all services offered here
    monday = db.Column(db.Boolean)
    tuesday = db.Column(db.Boolean)
    wednesday = db.Column(db.Boolean)
    thursday = db.Column(db.Boolean)
    friday = db.Column(db.Boolean)
    saturday = db.Column(db.Boolean)
    sunday = db.Column(db.Boolean)
    holiday = db.Column(db.Boolean)

    monday_open = db.Column(db.Integer)
    monday_close = db.Column(db.Integer)

    locations = db.relationship('Location', backref='hours')

    def __init__(self):
        monday = False
        tuesday = False
        wednesday = False
        thursday = False
        friday = False
        saturday = False
        sunday = False
        holiday = False

        monday_open = 9
        monday_close = 17

    def __repr__(self):
        return '<Business Hours: %r:00-%r:00 (%r)>' % (self.monday_open, self.monday_close, self.id)
