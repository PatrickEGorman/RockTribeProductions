from flask import render_template, g
from app import app
from app.db import models
from flask.ext.login import current_user


@app.before_request
def before_request():
    if current_user.is_authenticated():
        pass
    g.user = current_user


@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")


@app.route('/pictures')
def pictures():
    images = reversed(models.Picture.query.all())
    return render_template("pictures/Pictures.html", pictures=images)


@app.route('/videos')
def videos():
    video_clips = models.Video.query.all()
    return render_template("videos/Videos.html", videos=video_clips)


@app.route('/about')
def about():
    return render_template("About.html")


@app.route('/contact')
def contact():
    return render_template("Contact.html")


@app.route('/picture<picture_id>')
def enlarge(picture_id):
    image = models.Picture.query.get(picture_id)
    return render_template("pictures/zoom_picture.html", picture=image)

