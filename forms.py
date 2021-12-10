from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, AnyOf, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    
    name = StringField("Pet name")
    species = StringField("Species", validators=[AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField("Photo Url", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets"""
    
    photo_url = StringField("Photo Url", validators=[URL(), Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")