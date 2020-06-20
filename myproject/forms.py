# Flask based imports
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import DataRequired,EqualTo,Email,Length,Optional
from wtforms import ValidationError
from flask_wtf.file import FileAllowed,FileField

# User based imports
from flask_login import current_user
from myproject.models import User

from wtforms import DateTimeField
from wtforms.fields.html5 import DateTimeLocalField
from datetime import datetime

class AddEventForm(FlaskForm):
    dtf=DateTimeLocalField('Enter date and time')
    
    
    
class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    name=StringField('Name',validators=[DataRequired()])
    contact_no=StringField('Contact No',validators=[Length(min=10,max=10,message='Contact number should be 10 digits'),Optional()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password',message='Passwords did not match')])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Register')
    
    # validate_<fieldname>  method will automatically validate
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(message='Email has already registered! Please Log In!')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')
    
    def validate_password(self,field):
        user=User.query.filter_by(email=self.email.data).first()
        if user:
            if not user.validate_password(field.data):
                raise ValidationError(message='Password is incorrect')
        else: 
            raise ValidationError(message='Email does not exist')
        
        
        
class AddEventForm(FlaskForm):
    title=StringField('Task Title ',validators=[DataRequired()])
    scheduler_time=DateTimeLocalField('Time for the Task',validators=[DataRequired()],default=datetime.now, format='%Y-%m-%dT%H:%M')
    submit=SubmitField('Add Task')
    
    
            