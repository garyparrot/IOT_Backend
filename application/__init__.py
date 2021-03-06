from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_mgr = LoginManager()

def create_app(devTarget = "debug"):

    app = Flask(__name__, instance_relative_config = False, static_folder = None)

    # Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_mgr.init_app(app)

    with app.app_context():

        from . import routes

        # Create tables for our models
        db.create_all()

        app.register_blueprint(routes.auth_bp)
        app.register_blueprint(routes.dashboard_bp)
        app.register_blueprint(routes.api_bp)

        return app
