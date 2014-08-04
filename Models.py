from RockTribe import db


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String, index=True, unique=True)
    title = db.Column(db.String, unique=True)

    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    def __repr__(self):
        return '<Image %s>' % self.title


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String, index=True, unique=True)
    title = db.Column(db.String, unique=True)

    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    def __repr__(self):
        return '<Video %s>' % self.title