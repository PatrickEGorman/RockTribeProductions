from app import app
from flask import render_template, redirect
from app.db import models, db
from app.users.models import User
from app.users.comments.forms import Comment
from app.users.comments.models import PictureComment, VideoComment
from flask.ext.login import login_required

@app.route('/pictures', methods=["GET", "POST"])
def pictures():
    form = Comment()
    users = User.query.all()
    images = reversed(models.Picture.query.all())
    comments = PictureComment.query.all()
    return render_template("pictures/Pictures.html", pictures=images, form=form, comments=comments, users=users)


@app.route('/videos')
def videos():
    form = Comment()
    video_clips = reversed(models.Video.query.all())
    users = User.query.all()
    comments = VideoComment.query.all()
    return render_template("videos/Videos.html", videos=video_clips, form=form, comments=comments, users=users)


@app.route('/picture<picture_id>', methods=["GET", "POST"])
def enlarge(picture_id):
    form = Comment()
    image = models.Picture.query.get(int(picture_id))
    comments = reversed(PictureComment.query.filter_by(picture_id=picture_id).all())
    users = User.query.all()
    return render_template("pictures/zoom_picture.html", picture=image, form=form, comments=comments, users=users)


@app.route('/video<video_id>', methods=["GET", "POST"])
def enlarge_video(video_id):
    form = Comment()
    video = models.Video.query.get(int(video_id))
    comments = reversed(VideoComment.query.filter_by(video_id=video_id).all())
    users = User.query.all()
    return render_template("videos/preview_video.html", video=video, form=form, comments=comments, users=users)


@login_required
@app.route('/post_comment<id>', methods=["GET", "POST"])
def comment(id):
    form = Comment()
    if id[0] == 'p':
        comment = PictureComment(form.body.data, form.id.data)
        db.session.add(comment)
        db.session.commit()
        return redirect('/picture'+str(form.id.data))
    elif id[0] == 'v':
        comment = VideoComment(form.body.data, form.id.data)
        db.session.add(comment)
        db.session.commit()
        return redirect('/video'+str(form.id.data))
