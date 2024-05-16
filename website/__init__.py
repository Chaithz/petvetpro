from flask import Flask
import petml
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

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

    return app