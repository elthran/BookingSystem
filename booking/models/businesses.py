# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from booking.models.bases import Base, db

# Define a User model
class Business(Base):

    # Name of the business
    name = db.Column(db.String(128), nullable=False, unique=True)

    # List of all admins of the business
    admin_ids = db.Column(db.String(128), nullable=False)

    # List of all non-admins of the business
    employee_ids = db.Column(db.String(128), nullable=False)


    def __init__(self, admin_ids="", employee_ids=""):

        self.name = name

    def __repr__(self):
        return '<Business %r (ID: %r)>' % (self.name, self.id)
