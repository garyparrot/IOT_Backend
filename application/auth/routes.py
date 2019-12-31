from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField
from wtforms.validators import DataRequired
from ..models import db, User
from flask_login import login_user
from .. import login_mgr
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__,
                        template_folder = 'templates',
                        static_folder = 'static',
                        static_url_path = "/login/static")

"""
Login form for flaskWTF
"""
class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    username = StringField('username', [ DataRequired() ])
    password = StringField('password', [ DataRequired() ])

class SignForm(FlaskForm):
    class Meta:
        csrf = False
    username = StringField('username', [ DataRequired() ])
    password = StringField('password', [ DataRequired() ])

@auth_bp.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            if username and password:
                user = User.query.filter(User.username == username and User.password == password).first()
                if user:
                    return redirect(url_for('dashboard_bp.dashboard'))
        flash("Login Failed")
        return redirect(url_for('auth_bp.login'))

    return render_template("/login.html", form = form)

@auth_bp.route('/signup', methods = ['GET', 'POST'])
def signup():
    
    # Test if the cookie match the freaking secret
    # TODO: Remove this code, it is here for testing propose.
    if request.cookies.get('X-UPLOAD-SECRET','') != app.config['UPLOAD_SECRET']:
        return "Stay back", 401

    form = SignForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            existing_user = User.query.filter_by(username = username).first()
            if existing_user == None:
                adduser = User(username = username, passhash = generate_password_hash(password, method='sha256'))
                db.session.add(adduser)
                db.session.commit()
                login_user(adduser)
                return redirect(url_for("dashboard_bp.dashboard"))
            else:
                flash("This username already been used.")

    return render_template("/signup.html", form = form)

@auth_bp.route('/success', methods=['GET'])
@login_required
def success():
    return "Success"

@auth_bp.route('/failure', methods=['GET'])
def failure():
    return "You are not welcome"

@login_mgr.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_mgr.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view that page.")
    return redirect(url_for('auth_bp.login'))
