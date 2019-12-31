from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)

    username = db.Column(db.String(30), index=True , unique=True , nullable=False)
    passhash = db.Column(db.String(200), index=False, unique=False, nullable=False)

    def set_password(self, password):
        self.passhash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.passhash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
