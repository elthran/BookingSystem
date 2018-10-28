from booking.models.bases import db


class AnalyticEvent(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    server_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer)
    activity = db.Column(db.String(16))
    validity = db.Column(db.Boolean)

    def __init__(self, user_id=-1, activity="unknown"):
        self.user_id = user_id
        self.activity = activity
        self.validity = self.validate

    @property
    def validate(self):
        raise NotImplementedError


class AuthenticationEvent(AnalyticEvent):

    session_length = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session_length = 0

    @property
    def validate(self):
        if not isinstance(self.user_id, int):
            return False
        if not isinstance(self.activity, str) or self.activity not in ['login', 'logout']:
            return False
        return True


class TransactionEvent(AnalyticEvent):

    currency = db.Column(db.String(16))
    currency = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.currency = "CAD"
        self.amount = 0

    @property
    def validate(self):
        if not isinstance(self.user_id, int):
            return False
        if not isinstance(self.activity, str) and self.activity not in ['purchase', 'refund']:
            return False
        if not isinstance(self.currency, str) and self.currency not in ['CAD']:
            return False
        if not isinstance(self.amount, int):
            return False
        return True


class UnvalidatedEvent(AnalyticEvent):

    def __init__(self, table="unknown", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table = table

    @property
    def validate(self):
        return False