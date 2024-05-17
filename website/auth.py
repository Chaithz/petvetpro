from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth', __name__)

@auth.route('/index')
def index():
    return render_template("index.html")

# @auth.route('/secpage')
# def secpage():
#     return render_template("secpage.html")

@auth.route('/health_tips')
def health_tips():
    return render_template("health_tips.html")

@auth.route('/chat')
def chat():
    return render_template("chat.html")

@auth.route('/contact')
def contact():
    return render_template("contact.html")

@auth.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@auth.route('/petsday')
def petsday():
    return render_template("petsday.html")

@auth.route('/login',methods=['GET','POST'])
def login():
   
    return render_template("login.html", boolean=True)

@auth.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 1:
            flash('Email must be greater than 1 character!', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character!', category='error')
        elif len(password1) < 6:
            flash('Password must be atleast 6 characters!', category='error')
        elif password1 != password2:
            flash('Passwords dont match!', category='error')
        else:
            #add user to database
            flash('Account created successfully!', category='success')

    return render_template("sign_up.html")