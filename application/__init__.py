from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(devTarget = "debug"):

    app = Flask(__name__, instance_relative_config = False, static_folder = None)

    # Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():

        from . import routes

        # Create tables for our models
        db.create_all()

        app.register_blueprint(routes.login_bp)
        app.register_blueprint(routes.dashboard_bp)

        return app
