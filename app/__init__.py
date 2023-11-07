from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
# TODO: (milestone 3) import LoginManager and Moment extensions here

db = SQLAlchemy()
bootstrap =Bootstrap()
login = LoginManager()
login.login_view= 'auth.login'
moment = Moment()
# TODO: (milestone 3) create LoginManager object and configure the login view as 'auth.login', i.e, `login` route in `auth` Blueprint. 
# TODO: (milestone 3) create Moment object

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER 
    app.template_folder = config_class.TEMPLATE_FOLDER

    db.init_app(app)
    login.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    # blueprint registration
    from app.Controller.auth_routes import bp_auth as auth
    app.register_blueprint(auth)
    from app.Controller.routes import bp_routes as routes
    app.register_blueprint(routes)

    if not app.debug and not app.testing:
        pass
        # ... no changes to logging setup

    return app
