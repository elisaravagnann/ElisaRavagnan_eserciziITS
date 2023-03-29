from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, DateField, SelectField, IntegerField, TimeField, TextAreaField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError,  NumberRange
from ristorante.models import User
from flask_login import current_user



#COSTRUZIONE DEL FORM REGISTER
class RegistrationForm(FlaskForm):
    username = StringField('Nome Utente', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match'), Length(min=10)])
    confirm_password = PasswordField('Conferma la Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')   



#Funzione di verifica se un Email in base al numero e composizione dei suoi caratteri
import re

email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def is_valid_email(email):
    if re.search(email_regex, email):
        return True
    else:
        return False
    

#Funzione di verifica Password
def password_check(password):
    #Se ha minimo 10 caratteri
    if len(password) < 10:
        return False, 'La password deve contenere almeno 10 caratteri.'
    
    #Se ha almeno una lettera maiuscola
    if not re.search('[A-Z]', password):
        return False, 'La password deve contenere almeno una lettera maiuscola.'
    
    #Se ha almeno un carattere speciale
    if not re.search('[@_!#$%^&*()<>?/\|}{~:]', password):
        return False, 'La password deve contenere almeno un carattere speciale.'
    
    return True, 'La password Ã¨ valida.'    
         

#----------------------------------------------------------------------------------------
#COSTRUZIONE DEL FORM LOGIN
class LoginForm(FlaskForm):
    username = StringField('Nome Utente', validators=[DataRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Login')





 
    
    




