from flask import Blueprint, render_template
from flask import current_app as app
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

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
    name   = StringField('username', [ DataRequired() ])
    passwd = StringField('password', [ DataRequired() ])

@login_bp.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for('success'))

    return render_template("/login.html", form = form)

@login_bp.route('/success', methods=['GET'])
def success():
    return "Success"
