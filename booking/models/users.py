from booking.models.bases import Base, db
from werkzeug import generate_password_hash, check_password_hash

class User(Base):
    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    # Business associated with the user
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    def __init__(self, email, password, business_id):
        self.email = email
        self.set_password_hash(password)
        self.business_id = business_id

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

