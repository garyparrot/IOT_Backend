from flask import Blueprint, request, render_template, redirect, url_for
from flask import current_app as app

dashboard_bp = Blueprint('dashboard_bp', __name__,
                            template_folder = "templates",
                            static_folder = "static",
                            static_url_path = "/")

@dashboard_bp.route('/')
def dashboard():
    return render_template("index.html")
