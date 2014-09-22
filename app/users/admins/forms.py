from wtforms import StringField, Form
from wtforms.validators import DataRequired


class AddObject(Form):
    title = StringField('title', validators=[DataRequired()])
    url = StringField('url', validators=[DataRequired])
    description = StringField('description', validators=[DataRequired])
