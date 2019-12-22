from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(devTarget = "debug"):

    app = Flask(__name__, instance_relative_config = False)

    # Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():

        from . import routes

        app.register_blueprint(routes.login_bp)

        return app