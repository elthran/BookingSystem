from booking.models.bases import Base, db


class Business(Base):
    # Name of the business
    name = db.Column(db.String(128), nullable=False)

    # List of all admins ids of the business
    admin_ids = db.Column(db.String(128), nullable=False)

    # List of all non-admins ids of the business
    employee_ids = db.Column(db.String(128), nullable=False)

    # List of every appointment
    appointments = db.relationship('Appointment', backref='business')

    # List of every user
    users = db.relationship('User', backref='business')

    def __init__(self, name):
        self.name = name
        self.admin_ids = ""
        self.employee_ids = ""

    def __repr__(self):
        return '<Business %r (ID: %r)>' % (self.name, self.id)
