from booking.models.bases import db


class Mapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, business_id, location_id, user_id):
        self.business_id = business_id
        self.location_id = location_id
        self.user_id = user_id
