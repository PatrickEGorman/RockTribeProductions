from functools import wraps
from flask import render_template, request, redirect
from flask.ext.login import current_user
from app import app
from app.db import db
from app.db.models import Picture, Video
from app.users.admins import forms


def admin_check(func):
    @wraps(func)
    def admin_check_function(*args, **kwargs):
        try:
            if current_user.role == 1:
                function = func(*args, **kwargs)
            else:
                function = redirect('/home')
        except AttributeError:
            function = redirect('/home')
        return function
    return admin_check_function


@app.route('/submit', methods=['GET', 'POST'])
@admin_check
def submit():
    form = forms.AddObject()
    return render_template('pictures/submit.html', form=form)


@app.route('/preview', methods=['GET', 'POST'])
@admin_check
def add_preview():
    global picture
    picture = Picture(request.form['title'], request.form['url'], request.form['description'])
    return render_template("pictures/zoom_picture.html", picture=picture, picture_add=True)


@app.route('/add_picture')
@admin_check
def add_picture():
    try:
        db.session.add(picture)
        db.session.commit()
        return redirect('/pictures')
    except db.UniqueConstraint:
        db.session.rollback()
        return "error"

@app.route('/remove_image')
@admin_check
def remove():
    pictures = reversed(Picture.query.all())
    return render_template('user_accounts/admins/remove_picture.html', pictures=pictures)

@app.route('/preview<picture_id>')
@admin_check
def remove_preview(picture_id):
    global picture
    picture = Picture.query.filter_by(id=picture_id).first()
    return render_template("pictures/zoom_picture.html", picture=picture, picture_remove=True)

@app.route('/remove_picture')
@admin_check
def remove_picture():
    db.session.delete(picture)
    db.session.commit()
    return redirect('/pictures')

@app.route('/video_form', methods=['GET', 'POST'])
@admin_check
def video_form():
    form = forms.AddObject()
    return render_template('videos/add_video.html', form=form)

@app.route('/preview_video', methods=['GET', 'POST'])
@admin_check
def preview_video():
    global video
    video = Picture(request.form['title'], request.form['url'], request.form['description'])
    return render_template("videos/preview_video.html", video=video, video_add=True)

@app.route('/add_video')
@admin_check
def add_video():
    try:
        db.session.add(video)
        db.session.commit()
        return render_template('videos/Videos.html')
    except db.UniqueConstraint:
        return render_template('error.html', error=db.UniqueConstraint)