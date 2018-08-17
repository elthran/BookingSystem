from booking.models.bases import Base, db


class Email(Base):
    # Identification Data: email & password
    address = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(128), nullable=False)
    sent = db.Column(db.Boolean, nullable=False)

    def __init__(self, address, content):
        self.address = address
        self.content = content
        self.sent = False

    def __repr__(self):
        return '<Message: %r (To address %r [Sent: %r])>' % (self.content, self.address, self.sent)

