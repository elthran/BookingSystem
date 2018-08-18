from booking.models.bases import Base, db


class ContactEmail(Base):
    # Identification Data: email & password
    sender_email = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(128), nullable=False)
    sent = db.Column(db.Boolean, nullable=False)

    def __init__(self, sender_email, content):
        self.sender_email = sender_email
        self.content = content
        self.sent = False

    def __repr__(self):
        return '<Message: %r (From: %r [Sent: %r])>' % (self.content, self.sender_email, self.sent)

