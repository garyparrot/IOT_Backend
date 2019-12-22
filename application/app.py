from flask import Flask, url_for, render_template, request, Response, redirect
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

from wtforms import StringField
from wtforms.validators import DataRequired

def create_app(devTarget = "debug"):

    app = Flask(__name__, instance_relative_config = False)

    # Configuration
    config = 'config.DebugConfig' if lower(devTarget) == "debug" else "config.ReleaseConfig"
    app.config.from_object(config)

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():

        from . import routes

        app.register_blueprint(login_routes.login_bp)

        return app
