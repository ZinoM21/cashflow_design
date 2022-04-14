from flask import Blueprint, get_flashed_messages, redirect, render_template, url_for, request, current_app

blueprint = Blueprint('simple_pages', __name__)


### ROOT ###

@blueprint.route('/')
def root():
    get_flashed_messages()
    return render_template("simple_pages/root.html")

@blueprint.route('/home')
def home():
    return redirect(url_for('simple_pages.root'))


### FAQ ###

@blueprint.get('/faq')
def get_faq():
    return render_template('simple_pages/faq.html')

