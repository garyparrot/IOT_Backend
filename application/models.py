from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(30), index=True , unique=True , nullable=False)
    passhash = db.Column(db.String(80), index=False, unique=False, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
