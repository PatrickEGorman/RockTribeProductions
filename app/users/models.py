from app.db import db
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(15))
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    pictures = db.relationship('Picture', backref='user', lazy='dynamic')
    videos = db.relationship('Video', backref='user', lazy='dynamic')

    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, body, user_id):
        self.body = body
        self.user_id = user_id
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % self.body


