from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, IntegerField, SubmitField

class RecipeForm(FlaskForm):
    name = StringField('Recipe Name')
    ingredients = TextAreaField('Ingredients')
    steps = TextAreaField('Steps')
    preparation_time = IntegerField('Preparation Time (minutes)')
    image = FileField('Recipe Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Add Recipe')
