from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'AABBCCDDEEsjdsfklsdjdjdjsiw'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////database/database.sqlite'
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return redirect('/login', code=302)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    if(request.method == 'GET'):
        return render_template('signup.html', form=form)
    elif(request.method == 'POST'):
        if form.validate_on_submit():
            return 'form validated'
        else:
            return 'form did not validate'

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True)
