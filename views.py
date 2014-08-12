from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
app.debug = True
db.create_all()


@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")


@app.route('/pictures')
def pictures():
    import models
    images = models.Picture.query.all()
    for image in images:
        if "facebook" in image.url:
            images.remove(image)
    return render_template("Pictures.html", pictures=images)


@app.route('/videos')
def videos():
    import models
    videoclips = models.Video.query.all()
    for video in videoclips:
        if "http://" not in video.url:
            video.url = "http://"+video.url
        if "<br>" in video.description:
            video.description = video.description.replace("<br>", "")
    return render_template("Videos.html", videos=videoclips)


@app.route('/about')
def about():
    return render_template("About.html")


@app.route('/contact')
def contact():
    return render_template("Contact.html")

if __name__ == '__main__':
    app.run()
