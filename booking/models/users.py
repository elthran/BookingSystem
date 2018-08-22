from booking.models.bases import Base, db
from werkzeug import generate_password_hash, check_password_hash
from flask import url_for, request
from booking.models.locations import Location
from datetime import time


class User(Base):
    # Identification Data: email & password
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    phone = db.Column(db.Integer)
    # Business associated with the user
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    # Location default for user
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    # Appointments associated with the user
    appointments = db.relationship('Appointment', backref='user')
    # Availabilities that the employee has
    availabilities = db.relationship('Availability', backref='user')
    # Used for login_manager
    is_authenticated = db.Column(db.Boolean)  # They have filled in all required fields
    is_active = db.Column(db.Boolean)  # Account activated and not currently suspended
    is_anonymous = db.Column(db.Boolean)  # If account is anonymous
    # Permissions
    is_owner = db.Column(db.Boolean)  # Determines if they are an 'owner' of the business. Grants full permissions
    is_manager = db.Column(db.Boolean)  # Determines if they have full control over a location
    # Used for email verification
    is_verified = db.Column(db.Boolean)

    def __init__(self, name, email, password, business_id, is_owner):
        self.name = name
        self.email = email
        self.set_password_hash(password)
        self.phone = 0000000000
        self.business_id = business_id
        self.is_owner = is_owner
        self.is_manager = False
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
        self.is_verified = False
        self.location_id = 1

    def __repr__(self):
        return '<User %r (%r)>' % (self.email, self.id)

    # Custom property reminder
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute. Only password_hash is stored.')

    # Custom property setter
    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    # Password verifier. Can send in a plain password and it will compare it to the hashed password.
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    def generate_verification_link(self):
        return str(self.id) + "-" + self.name

    def get_verification_link(self):
        return request.url_root[:-1] + url_for('verification', id=self.id, verification_link=self.generate_verification_link())

    def check_verification_link(self, link):
        if link == request.url_root[:-1] + (str(self.id) + "-" + self.name):
            print("verified")
            return True
        print("verification failed")
        return False

    def get_availability_by_day(self, day):
        return [availability for availability in self.availabilities if availability.day == day]

    @property
    def location(self):
        return Location.query.get(self.location_id)

    def sorted_availabilities(self, day=None):
        """
        Returns availabilities sorted first by day, then by start time. You can pass in one specific day to check.
        """
        if day is not None:
            availabilities = [availability for availability in self.availabilities if availability.day == day]
        else:
            availabilities = self.availabilities
        return sorted(availabilities, key=lambda x: (x.day, x.start))

    def verify_time_value(self, hour, minute):
        """
        This function lets you pass in hours greater than 23 and minutes 60 or above.
        """
        new_hour = (hour % 24) + (minute // 60)
        new_minute = (minute % 60)
        return new_hour, new_minute

    def working_hours_by_day(self, day):
        """
        This creates a list of all hours that a user is working on any given day.
        Currently this function isnt used anywhere, but it will be used to generate the visuals.
        Feel free to run this function and it'll tell you all hours that the user is busy.
        """
        availabilities = self.sorted_availabilities(day)
        options = []
        if not availabilities:
            return 0
        for availability in availabilities:
            count = 0
            while True:
                new = time(availability.start.hour + count, 0)
                options.append((new.hour, new.__str__()))
                count += 1
                if new >= availability.end:
                    break
        return options

    def available_hours_by_day(self, day, condition):
        """
        This creates a list of hours that a user DOESN'T work in a day.
        That way you can run this function in JSON to have the menus update when you choose a day,
        and let you choose hours that you are available.
        """
        if condition == "close":
            pass
        all_hours = [i for i in range (28)]
        if self.availabilities == []:
            # Need to return this first or it will crash when it cant iterate through an empty list
            return [(i,str(i)+":00") for i in range(23)]
        busy_hours = [i[0] for i in self.working_hours_by_day(day)]
        available_hours = [i for i in all_hours if i not in busy_hours]
        options = []
        for i in available_hours:
            if condition == "open":
                hour, minute = self.verify_time_value(i, 0)
            else:
                hour,minute = self.verify_time_value(i + 1,0)
            hour = time(hour, minute).hour
            options.append((hour,str(hour)+":00"))
        return options


