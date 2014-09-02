from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

"""This is a module holding form objects"""

# aboutMe form asking for a name from the user
class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    breed = StringField('What is your breed?')
    submit = SubmitField('Submit form')

    # function making validators work
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(NameForm, self).__init__(*args, **kwargs)