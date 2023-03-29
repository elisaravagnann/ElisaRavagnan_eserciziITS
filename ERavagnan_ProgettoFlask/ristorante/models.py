from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from ristorante import db, login_manager
from flask_bcrypt import Bcrypt


#Tabella degli utenti del database del sito
#Funzione che carica l'oggetto utente dal database in base all'ID utente.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        """Funzione per generare l'hash della password e impostarla"""
        self.password = generate_password_hash(password)

    @staticmethod
    def password_check(password):
        """
        Funzione che controlla la validità della password.
        Controlla se la password rispetta i requisiti:
        - almeno 8 caratteri
        - almeno una lettera minuscola
        - almeno una lettera maiuscola
        - almeno un numero
        - almeno un carattere speciale tra !@#$%^&*
        """
        if len(password) < 8:
            return False, 'La password deve contenere almeno 8 caratteri.'
        elif password.isalpha():
            return False, 'La password deve contenere almeno un carattere numerico o un simbolo.'
        elif password.isnumeric():
            return False, 'La password deve contenere almeno una lettera o un simbolo.'
        else:
            return True, 'La password è valida.'

    def check_password(self, password):
        if not self.password:
            return False
        return check_password_hash(self.password, password)


#Database delle recensioni
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Review {}>'.format(self.id)




    
    
    
    





