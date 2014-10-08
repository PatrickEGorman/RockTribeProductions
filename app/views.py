from flask import render_template, g
from app import app
from users import login_manager
from users.models import User


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")


@app.route('/about')
def about():
    return render_template("About.html")


@app.route('/contact')
def contact():
    return render_template("Contact.html")


