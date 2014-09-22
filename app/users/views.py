import operator
from flask import render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user, login_required, current_user
from app import app
from app.db import db
from app.users import models, forms, login_manager


@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(userid):
    return models.User.query.filter_by(id=userid)


@app.route('/create_account', methods=['GET', 'POST'])
def create():
    form = forms.User()
    if form.validate_on_submit():
        user = models.User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
            name=form.name.data
        )
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect('/home')
        except BaseException:
            return render_template('error.html', error="Username or email already exists.")
    return render_template('user_accounts/create.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = form.get_user()
        login_user(user, remember=True)
        flash("Logged in successfully.")
        return redirect('/home')
    return render_template('user_accounts/login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/home')

try:
    if current_user.is_authenticated() and current_user.role == 1:
        from app.users.admins import views
except AttributeError:
    pass


@app.route("/userposts")
def users():
    posts = models.Post.query.all()
    users = models.User.query.all()
    posts.sort(key=operator.attrgetter('timestamp'))
    return render_template('user_accounts/posts.html', posts=posts, users=users)


@app.route("/create_post")
@login_required
def create_post():
    form = forms.Post
    if form.validate_on_submit():
        post = models.Post(form.body.data, models.User.get_id(g.user.id))
        db.session.add(post)
        db.session.commit()
        return redirect('/userposts')
    return render_template('useraccounts/create_post.html', form=form)



