from flask import Flask, url_for, render_template, request, Response, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from .login import routes as login_routes

# Flask configuration
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Registe blueprints
app.register_blueprint(login_routes.login_bp)
