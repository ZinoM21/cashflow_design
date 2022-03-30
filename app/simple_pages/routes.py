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

@blueprint.get('/signup')
def get_signup():
    # Log:
    print('YOU ARE NOW ABLE TO SIGN UP')

    return render_template("simple_pages/signup.html")

@blueprint.post('/signup')
def post_signup():
    # Log:
    print('YOUR DATA WAS UPLOADED')
    
    create_user(request.form)

    return render_template('simple_pages/account.html')