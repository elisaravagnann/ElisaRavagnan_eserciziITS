from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages, session
from ristorante import app, db, bcrypt
from ristorante.forms import RegistrationForm, password_check, is_valid_email, LoginForm
from ristorante.models import User, Review
from flask_login import login_user, logout_user, current_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_babel import gettext
import hashlib
from datetime import datetime


#App di home
@app.route("/")
@app.route("/home")
def home():
    message = session.pop('message', None)
    return render_template("home.html", message=message)



#App di Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Username o password non validi', 'error')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('home'))
    return render_template('login.html', title='Accedi', form=form, _=gettext)






#App di Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
          #Controlli sui campi del form
          #Riprendo la funzione is_valid_email
          if not is_valid_email(form.email.data):
               flash('Email non valida.', 'danger')
               return render_template('register.html', title='Register', form=form, _=gettext)
          #Riprendo la funzione password_check
          if not password_check(form.password.data)[0]:
               flash('Password non valida.', 'danger')
               return render_template('register.html', title='Register', form=form, _=gettext)
          #Condizione per verificare se password e conferma password corrispondono
          if form.password.data != form.confirm_password.data:
               flash('Le password non corrispondono.', 'danger')
               return render_template('register.html', title='Register', form=form, _=gettext)
          #Condizione per verificare se un Username ÃƒÂ¨ giÃƒÂ  stato utilizzato
          if User.query.filter_by(username=form.username.data).first() is not None:
               flash('Utente giÃ Â  registrato.', 'danger')
               return render_template('register.html', title='Register', form=form, _=gettext)
          #Condizione per verificare se un'Email ÃƒÂ¨ giÃƒÂ  stata utilizzata
          if User.query.filter_by(email=form.email.data).first() is not None:
               flash('Email giÃ Â  registrata.', 'danger')
               return render_template('register.html', title='Register', form=form, _=gettext)
          #Fine controlli sui campi del form
          
          #Se l'utente Ã¨ stato registrato con successo, esegui il login e mostra la navbar con le info 
          #dell'utente
          user = User(username=form.username.data, email=form.email.data)
          user.set_password(form.password.data)
          db.session.add(user)
          db.session.commit()
          
          flash('Registrazione avvenuta con successo!', 'success')
          login_user(user)  #Segue il login dell'utente appena registrato
          return redirect(url_for('home', _anchor=''))
    return render_template('register.html', title='Register', form=form)


#App di Logout
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


#---------------------------------------------------------------------------------

#App di Submit Review
@app.route('/submit_review', methods=['POST'])
@login_required
def submit_review():
    stars = request.form.get('stars')
    text = request.form.get('text')

    if stars and text:
        review = Review(stars=stars, text=text, user_id=current_user.id)
        db.session.add(review)
        db.session.commit()

    return redirect(url_for('reviews'))


#App di Review
@app.route('/reviews')
def reviews():
    reviews = Review.query.join(User).order_by(Review.date_posted.desc()).all()
    return render_template('reviews.html', reviews=reviews)

#----------------------------------------------------------------------------------















