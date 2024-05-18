from flask import Blueprint,render_template,request,flash,redirect,url_for
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/index')
def index():
    return render_template("index.html")

# @auth.route('/secpage')
# def secpage():
#     return render_template("secpage.html")

@auth.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', category='error')
        elif  len(email) <2:
            flash('Email must be greater than 1 character!', category='error')
        elif len(firstname) < 2:
            flash('Name must be greater than 1 character!', category = 'error')
        elif len(password1) < 6:
            flash('Password must be atleast 6 character!', category = 'error')
        elif password1 != password2:
            flash('Password Mismatch!', category = 'error')
        else:
            new_user =User(email=email, firstname=firstname,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)

            flash('Account created successfully!', category = 'success')
            return redirect(url_for('views.home'))
        
    return render_template("register.html",user=current_user)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.write'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("register.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))