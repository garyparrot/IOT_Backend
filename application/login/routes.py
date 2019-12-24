from flask import Blueprint, request, render_template, redirect, url_for
from flask import current_app as app
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from ..models import db, User

login_bp = Blueprint('login_bp', __name__,
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

@login_bp.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        if username and password:
            user = User.query.filter(User.username == username and User.password == password).first()
            if user:
                return redirect(url_for('login_bp.success'))
        return redirect(url_for('login_bp.failure'))

    return render_template("/login.html", form = form)

@login_bp.route('/success', methods=['GET'])
def success():
    return "Success"

@login_bp.route('/failure', methods=['GET'])
def failure():
    return "You are not welcome"

