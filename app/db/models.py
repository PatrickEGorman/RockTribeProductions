from app.db import db
from flask.ext.login import current_user


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String)
    title = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('PictureComment', backref='picture', lazy='dynamic')

    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description
        self.user_id = current_user.id

    def __repr__(self):
        return '<Image %s>' % self.title


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String, index=True)
    title = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('VideoComment', backref='picture', lazy='dynamic')

    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description
        self.user_id = current_user.id

    def __repr__(self):
        return '<Video %s>' % self.title


class AdminPassword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)



