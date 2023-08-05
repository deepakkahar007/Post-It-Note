from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import Length,DataRequired

class CreateNotes(FlaskForm):
    title=StringField(label='Title : ',validators=[ DataRequired(),Length(max=30)] )
    description=StringField(label='Description : ',validators=[DataRequired(),])
    category=StringField(label='Category : ')    
    submit=SubmitField(label='Submit')

class RegisterUser(FlaskForm):
    name=StringField(label="Name : ",validators=[DataRequired()])
    email=EmailField(label="Email : ",validators=[DataRequired()])
    password=PasswordField(label="Password : ",validators=[DataRequired()])
    submit=SubmitField(label="Create Account")


class LoginUser(FlaskForm):
    email=EmailField(label="Email Address",validators=[DataRequired()])
    password=PasswordField(label="Password",validators=[DataRequired()])
    submit=SubmitField(label="Log In")