from booking.models.bases import Base, db


class Business(Base):
    # Name of the business
    name = db.Column(db.String(128), nullable=False, unique=True)

    # List of all admins ids of the business
    admin_ids = db.Column(db.String(128), nullable=False)

    # List of all non-admins ids of the business
    employee_ids = db.Column(db.String(128), nullable=False)

    # List of all current appointments (checks the appointment table for any which have a foreign key matching your business id
    appointments = db.relationship('Appointment', backref='business')

    def __init__(self, name):
        self.name = name
        self.admin_ids = ""
        self.employee_ids = ""

    def __repr__(self):
        return '<Business %r (ID: %r)>' % (self.name, self.id)
