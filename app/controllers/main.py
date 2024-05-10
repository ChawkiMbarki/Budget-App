""" 
    This file defines route handlers for main web pages such as home and about.
    It uses Flask Blueprints to organize and manage route endpoints and view functions.
"""

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """ Home Page """

    return render_template('index.html')

@main_bp.route('/login')
def login():
    """ login Page """

    return '<center><h1>login</h1></center>'

@main_bp.route('/sign_up')
def sign_up():
    """ sign up Page """

    return '<center><h1>Sign Up</h1></center>'

@main_bp.route('/about')
def about():
    """ about Page """

    return '<center><h1>About us</h1></center>'
