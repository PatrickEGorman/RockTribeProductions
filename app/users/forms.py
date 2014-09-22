from flask import g
from flask.ext.login import session
from flask.ext.wtf import Form
from wtforms import StringField, validators, IntegerField
from wtforms.validators import DataRequired
from app import app
from app.users import models
from app.db import db
from werkzeug.security import check_password_hash


class User(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    email = StringField('email')
    name = StringField('name')


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

    def validate_login(self):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(models.User).filter_by(username=self.username.data).first()


class Post(Form):
    body = StringField('body')
    user_id = IntegerField('user_id')