from views import db
from models import Picture, Video


class DbInit():

    def __init__(self):
        db.drop_all()
        db.create_all()
        picture1 = Picture(
            url="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-xfp1/t1.0-9/10303368_319268634903365_8162484403308547357_n.jpg",
            title = "Nick at New River Gorge National River",
            description="(Photo credit Mac Wood)")
        db.session.add(picture1)
        db.session.commit()

