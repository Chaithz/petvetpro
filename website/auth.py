from flask import Blueprint,render_template

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

