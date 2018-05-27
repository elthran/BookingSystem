# THIS SHOULD BE A DB.MODEL I BELIEVE

class User(object):

    # __tablename__ = 'user'

    # name = db.Column(db.String(128), nullable=False, unique=True)
    # password = db.Column(db.String(128), nullable=False)

    def __init__(self, name="Unknown"):
        self.name = name
        self.password = "0000"

    def __repr__(self):
        print("<User %r>") % (self.name)