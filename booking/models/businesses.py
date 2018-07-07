from booking.models.bases import Base, db
from flask import request, url_for
from datetime import datetime


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

    def get_clients(self):
        return [client for client in self.clients if client.email != "anonymous@hidden.com"]

    def get_todays_appointments(self):
        """
        Checks the date of each appointment (ignoring the time) and checks if it's today's date. Might bug out if the user is in a different timezone?
        @klondikemarlen please check if this is timezone compatible
        """
        return [appointment for appointment in self.appointments if appointment.date.date() == datetime.now().date()]

    def get_appointments_by_day(self, year, month, day):
        """
        You can choose a date and it returns all apointments for the business on that date
        This function is really messy
        """
        def correct_size(thing):
            if len(str(thing)) >= 2:
                return str(thing)
            else:
                return "0" + str(thing)
        date_check = correct_size(year) + "-" + correct_size(month) + "-" + correct_size(day)

        """
        I think it should probably look like this and be shorter, simpler.
        better_date = datetime.date(year, month, day)
        return [appointment for appointment in self.appointments if appointment.date.date() == better_date.date()]
        """

        return [appointment for appointment in self.appointments if str(appointment.date.date()) == date_check]

    def __repr__(self):
        return '<Business %r (ID: %r)>' % (self.name, self.id)
