from flask.ext.wtf import Form
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired


class Comment(Form):
    body = TextAreaField('body', validators=[DataRequired()])
    id = IntegerField('picture_id', validators=[DataRequired()])
