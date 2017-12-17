from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SignupForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

# initialize app and create db object

app = Flask(__name__)
app.secret_key = 'AABBCCDDEEsjdsfklsdjdjdjsiw'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///db/database.sqlite'
db = SQLAlchemy(app)

# initialize db with tables from models

from models import *
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()

# initialize login manager

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

@app.route('/', methods=['GET'])
def index():
    return redirect('/login', code=302)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignupForm()

    if(request.method == 'GET'):
        if(current_user.is_authenticated):
            return redirect('/panel')
        else:
            return render_template('login.html', form=form)
    elif(request.method == 'POST'):
        if(form.validate_on_submit()):
            user = User.query.filter_by(username=form.username.data).first()
            if(user):
                auth = False
                try:
                    auth = pbkdf2_sha256.verify(form.password.data, user.password)
                except Exception as e:
                    flash('Incorrect Password')
                    return redirect('/login')
                if(auth):
                    login_user(user)
                    return redirect('/panel')
                else:
                    flash('Incorrect Password')
                    logout_user()
                    return redirect('/login')
            else:
                flash('User does not exist')
                logout_user()
                return redirect('/login')
        else:
            flash('Incorrect information')
            logout_user()
            redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    if(request.method == 'GET'):
        return render_template('signup.html', form=form)
    elif(request.method == 'POST'):
        if form.validate_on_submit():
            if(User.query.filter_by(username=form.username.data).first()):
                flash('Username already exists')
                return redirect('/signup')
            else:
                password_hash = pbkdf2_sha256.hash(form.password.data)
                user = User(form.username.data, password_hash)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect('/panel')
        else:
            return 'form did not validate'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully')
    return redirect('/login')

@app.route('/panel')
@login_required
def panel():
    return render_template('homeNETPIE.html', user=current_user)

@login_manager.unauthorized_handler
def unauthorized():
    flash('Please login first.')
    return redirect('/login')

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True)
