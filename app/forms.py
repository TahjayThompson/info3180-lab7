from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    description = StringField('Message',validators=[DataRequired()])
