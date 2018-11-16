from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)


#initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

# Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
