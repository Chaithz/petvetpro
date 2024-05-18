from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Javamysql.25@localhost/petvetpro'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    # petml.load_csv()
    # petml.fill_missing_values(data)
    # petml.variables()
    # petml.model_train(X,y)
    # petml.inputs()
    # petml.prediction(affection,vaccinated,age,weight,appetite,injury,wound)
    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .model import User,Review

    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view ='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')





#app.config['MYSQL_HOST'] = "localhost"
#app.config['MYSQL_USER'] = "root"
#app.config['MYSQL_PASSWORD'] = ""
#app.config['MYSQL_DB'] = "petvetpro"# yet to create the databse
#mysql = MySQL(app)

#cur = mysql.connection.cursor()

#cur.execute("INSERT INTO doctor (name,email,password) VALUES (%s,%s)",(name,email,password))
#mysql.connection.commit()
#cur.close()
