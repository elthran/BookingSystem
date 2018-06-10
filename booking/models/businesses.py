from booking.models.bases import Base, db
from flask import request

class Business(Base):
    # Name of the business
    name = db.Column(db.String(128), nullable=False)

    # List of all admins ids of the business
    admin_ids = db.Column(db.String(128), nullable=False)

    # List of all non-admins ids of the business
    employee_ids = db.Column(db.String(128), nullable=False)

    # List of every appointment
    appointments = db.relationship('Appointment', backref='business')

    # List of every admin/employee user account registered to this business
    users = db.relationship('User', backref='business')

    # List of every service offered by this business
    services = db.relationship('Service', backref='business')

    # List of every client
    clients = db.relationship('Client', backref='business')

    def __init__(self, name):
        self.name = name
        self.admin_ids = ""
        self.employee_ids = ""

    def get_client_link(self):
        return request.url_root + "book_appointment/" + str(self.id)

    def get_employee_link(self):
        return request.url_root + "register_employee/" + str(self.id)

    def get_admins(self):
        return [user for user in self.users if user.is_admin]

    def get_employees(self):
        return [user for user in self.users if not user.is_admin]

    def __repr__(self):
        return '<Business %r (ID: %r)>' % (self.name, self.id)
