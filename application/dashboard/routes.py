from flask import Blueprint, request, render_template, redirect, url_for
from flask import current_app as app
from flask_login import login_required

dashboard_bp = Blueprint('dashboard_bp', __name__,
                            template_folder = "templates",
                            static_folder = "static",
                            static_url_path = "/")

@dashboard_bp.route('/')
@login_required
def dashboard():
    return render_template("index.html")
