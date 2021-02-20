         


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email



class ContactForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Subject = StringField('Subject', validators=[DataRequired()])
    Message = TextAreaField('Message', validators=[DataRequired()])

