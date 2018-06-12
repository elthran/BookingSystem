from booking.models.bases import Base, db


class Client(Base):
    email = db.Column(db.String(128), nullable=False, unique=True)
    name = db.Column(db.String(128))  # First and Last Name
    phone = db.Column(db.String(128), unique=True)
    contact_method = db.Column(db.String(128))

    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # List of every appointment
    appointments = db.relationship('Appointment', backref='client')

    def __init__(self, email, business_id):
        self.email = email
        self.business_id = business_id
        self.name = "Unknown"
        self.phone = None
        self.contact_method = None

    def __repr__(self):
        return '<Client %r (%r)>' % (self.email, self.id)
