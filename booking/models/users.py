from booking.models.bases import Base, db
from werkzeug import generate_password_hash, check_password_hash
from flask import url_for


class User(Base):
    # Identification Data: email & password
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    phone = db.Column(db.Integer)
    # Business associated with the user
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    # Appointments associated with the user
    appointments = db.relationship('Appointment', backref='user')
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
        return url_for('verification', user_id=self.id, verification_link=self.generate_verification_link())

    def check_verification_link(self, link):
        if link == (str(self.id) + "-" + self.name):
            return True
        return False
