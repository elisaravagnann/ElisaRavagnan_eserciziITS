from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_babel import Babel




#Crea l'oggetto app
app = Flask(__name__)
babel = Babel(app)
app.app_context().push()

#Imposto la chiave segreta dell'applicazione di flask
app.config['SECRET_KEY'] = '35f76991980ac9d1ec403f4391108054ae9ce824'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'


#Configurazione del sistema di messaggistica di Flask
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
Session(app)






db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from ristorante import routes, models


#Creiamo le tabelle
with app.app_context():
    db.create_all()






