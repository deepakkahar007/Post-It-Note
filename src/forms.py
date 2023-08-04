from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,DataRequired

class CreateNotes(FlaskForm):
    title=StringField(label='Title:',validators=[ DataRequired(),Length(max=30)] )
    description=StringField(label='Description',validators=[DataRequired(),])
    category=StringField(label='Category')    
    submit=SubmitField(label='Submit')

