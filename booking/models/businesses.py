from booking.models.bases import Base, db
from flask import request, url_for


class Business(Base):
    # Name of the business
    name = db.Column(db.String(128), nullable=False)
    # Referral code
    referral = db.Column(db.String(128), unique=True)
    # List of all admins ids of the business
    owner_ids = db.Column(db.String(128), nullable=False)
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
    # List of every location
    locations = db.relationship('Location', backref='business')

    def __init__(self, name):
        self.name = name
        self.owner_ids = ""
        self.employee_ids = ""
        self.set_referral_id()

    # Custom property setter
    def set_referral_id(self):
        self.referral = "ABCD" + self.name # I will make this create a unique and random referral string later using a function

    def check_referral(self, referral):
        return True

    def get_client_link(self):
        return request.url_root + "booking/appointment/" + str(self.id)

    def get_employee_link(self):
        return url_for('register_user', business_id=self.id, business_referral=self.referral)

    def get_employees(self):
        # Automatically sorts them so that admins are displayed first
        return [user for user in self.users if user.is_owner] + [user for user in self.users if not user.is_owner]

    def __repr__(self):
        return '<Business %r (ID: %r)>' % (self.name, self.id)
