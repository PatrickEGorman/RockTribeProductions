from flask.ext.wtf import Form
from wtforms import StringField, BooleanField


class LoginForm(Form):
    openid = StringField('openid')
    remember_me = BooleanField('remember_me', default = False)