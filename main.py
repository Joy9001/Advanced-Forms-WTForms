import os

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from flask_bootstrap import Bootstrap5

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    email = EmailField('Email',
                       [
                           DataRequired(message='Field cannot be empty!'),
                           Regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                                  message='Invalid email format. Example: example@example.com'),
                           Length(min=8, max=120, message='Email must be between 8 and 30 characters long.')
                       ])

    password = PasswordField('Password',
                             [
                                 DataRequired(message='Field cannot be empty!'),
                                 Length(min=8, message='Password must be at least 8 characters long.'),
                                 Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!*])[A-Za-z\d@#$%^&+=!*]{8,}$',
                                        message='Please enter a valid password with At least one uppercase letter, At least one lowercase letter, At least one digit, At least one speacial character')
                             ])
    login = SubmitField('Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if login_form.email.data == "jokeward369@gmail.com" and login_form.password.data == "Password@123":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
