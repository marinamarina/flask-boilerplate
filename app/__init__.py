from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
from werkzeug.contrib.fixers import ProxyFix


bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
#database representation
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #loading configurations into the app
    app.config.from_object(config[config_name])

    #initialise the application
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    #attach routes and custom error pages here
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app