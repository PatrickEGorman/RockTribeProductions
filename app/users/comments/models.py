from app.db import db
from app.users.models import User
from flask.ext.login import current_user


class PictureComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(length=250))
    user_id = db.Column(db.Integer)
    picture_id = db.Column(db.Integer, db.ForeignKey('picture.id'))

    def __init__(self, body, picture_id):
        self.body = body
        self.user_id = current_user.id
        self.picture_id = picture_id


class VideoComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(length=250))
    user_id = db.Column(db.Integer)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))

    def __init__(self, body, video_id):
        self.body = body
        self.user_id = current_user.id
        self.video_id = video_id


