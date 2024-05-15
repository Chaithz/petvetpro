from flask import Blueprint,render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/secpage')
def secpage():
    return render_template("secpage.html")

@views.route('/health_tips')
def health_tips():
    return render_template("health_tips.html")

@views.route('/chat')
def chat():
    return render_template("chat.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@views.route('/petsday')
def petsday():
    return render_template("petsday.html")