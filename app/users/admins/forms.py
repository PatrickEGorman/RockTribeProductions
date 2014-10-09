from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class AddObject(Form):
    title = StringField('title', validators=[DataRequired()])
    url = StringField('url', validators=[DataRequired])
    description = TextAreaField('description', validators=[DataRequired])


class RemoveVideo(Form):
    video_id = IntegerField('video_id', validators=[DataRequired()])


class MakeAdmin(Form):
    password = StringField('password', validators=[DataRequired()])