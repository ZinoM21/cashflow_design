from crypt import methods
from flask import Blueprint, redirect, render_template, url_for, request
from app.simple_pages.services.create_user import create_user

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def root():
    # Log:
    print('WELCOME HOME, SIR')

    return render_template("simple_pages/root.html")

@blueprint.route('/home')
def home():
    # Log:
    print('REDIRECT /home TO /')
    
    return redirect(url_for('simple_pages.root'))

@blueprint.get('/login')
def get_login():
    # Log:
    print('YOU ARE NOW ABLE TO LOG IN')

    return render_template("simple_pages/login.html")

@blueprint.post('/login')
def post_login():
    # Log:
    print('YOUR DATA WAS UPLOADED')

    return render_template("simple_pages/login.html")

@blueprint.route('/signup')
def get_signup():
    # Log:
    print('YOU ARE NOW ABLE TO SIGN UP')

    return render_template("simple_pages/signup.html")

@blueprint.get('/account')
def get_account():
    return render_template("simple_pages/account.html")

@blueprint.post('/account')
def post_account():
    # Log:
    print('YOUR DATA WAS UPLOADED')
    
    if not all([
        request.form.get('email'),
        request.form.get('password')
    ]):
        return render_template('simple_pages/signup.html', error="Please fill out all input fields to sign up!")

    create_user(request.form)
    return render_template("simple_pages/account.html")