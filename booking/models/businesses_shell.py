from booking.models.bases import Base, db


class BusinessShell(Base):
    name = db.Column(db.String(128))
    admin_ids = db.Column(db.String(128))

    def __init__(self, name):
        self.name = name
        self.admin_ids = ""

    def __repr__(self):
        return '<Business Shell %r (ID: %r)>' % (self.name, self.id)
