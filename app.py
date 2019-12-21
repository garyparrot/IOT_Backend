from flask import Flask, url_for, render_template, request, Response, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Flask configuration
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Login form
class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    name   = StringField('username', [ DataRequired() ])
    passwd = StringField('password', [ DataRequired() ])

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template("/login.html", form = form)

@app.route("/success")
def success():
    return "Success"
