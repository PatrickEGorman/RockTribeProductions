import operator
from flask import render_template, flash, redirect, g
from flask.ext.login import login_user, logout_user, login_required, current_user
from app import app
from app.db import db
from app.users import models, forms, login_manager


@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(int(userid))


@app.before_request
def before_request():
    g.user = current_user


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
        try:
            login_user(user, remember=True)
            flash("Logged in successfully.")
            return redirect('/home')
        except AttributeError:
            flash("Invalid username or password")
            redirect('/login')
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


@app.route("/userposts", methods=["GET", "POST"])
def users():
    form = forms.Post()
    posts = models.Post.query.all()
    user_list = models.User.query.all()
    posts.sort(key=operator.attrgetter('timestamp'))
    if form.validate_on_submit():
        post = models.Post(body=form.body.data, user_id=g.user.id)
        db.session.add(post)
        db.session.commit()
        return redirect('/userposts')
    return render_template('user_accounts/posts.html', posts=posts, users=user_list, form=form)



