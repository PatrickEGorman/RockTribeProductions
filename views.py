from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy()
db.init_app(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")


@app.route('/pictures')
def pictures():
    picture_query = database.Query()
    images = picture_query.querypictures()
    return render_template("Pictures.html", pictures=images)


@app.route('/videos')
def videos():
    return render_template("Videos.html")


@app.route('/about')
def about():
    return render_template("About.html")


@app.route('/contact')
def contact():
    return render_template("Contact.html")

if __name__ == '__main__':

    app.run()
