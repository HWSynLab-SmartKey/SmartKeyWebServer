from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy

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
        return render_template('login.html', form=form)
    elif(request.method == 'POST'):
        if(form.validate_on_submit()):
            user = User.query.filter_by(username=form.username.data).first()
            if(user):
                if(user.password == form.password.data):
                    login_user(user)
                    return 'User logged in'
                else:
                    return 'Incorrect Password'
            else:
                return 'User does not exist'
        else:
            return 'form did not validate'

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    if(request.method == 'GET'):
        return render_template('signup.html', form=form)
    elif(request.method == 'POST'):
        if form.validate_on_submit():
            if(User.query.filter_by(username=form.username.data).first()):
                return 'Username already exists'
            else:
                user = User(form.username.data, form.password.data)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return 'User created'
        else:
            return 'form did not validate'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'User logged out'

@app.route('/panel')
@login_required
def panel():
    return 'Protected'

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True)
