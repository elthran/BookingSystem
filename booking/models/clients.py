from booking.models.bases import Base, db


class Client(Base):
    email = db.Column(db.String(128))
    name = db.Column(db.String(128))  # First and Last Name
    phone = db.Column(db.String(128))
    contact_method = db.Column(db.String(128))
    consent_form = db.Column(db.Boolean) # Unused
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    # List of every appointment
    appointments = db.relationship('Appointment', backref='client')

    def __init__(self, email, business_id, name, phone="No phone number"):
        self.email = email
        self.business_id = business_id
        self.name = name
        self.phone = phone
        self.contact_method = None
        self.consent_form = False

    def __repr__(self):
        return '<Client %r (%r)>' % (self.email, self.id)
