from app import db

class User(db.Model):
    username = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(512))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)
