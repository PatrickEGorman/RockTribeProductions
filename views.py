from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

import models


@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")


@app.route('/pictures')
def pictures():
    images = models.Picture.query.all()
    return render_template("Pictures.html", pictures=images)


@app.route('/videos')
def videos():
    video_clips = models.Video.query.all()
    return render_template("Videos.html", videos=video_clips)


@app.route('/about')
def about():
    return render_template("About.html")


@app.route('/contact')
def contact():
    return render_template("Contact.html")

if __name__ == '__main__':

    app.run()
