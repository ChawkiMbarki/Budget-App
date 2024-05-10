""" 
This file defines route handlers for web pages related to the client such as profile.
It uses Flask Blueprints to organize and manage route endpoints and view functions.
"""

from app.models.user import User
from flask_bcrypt import Bcrypt
from flask import Blueprint, redirect, request, render_template, url_for, session, flash

user_bp = Blueprint('user', __name__)
bcrypt = Bcrypt()

@user_bp.route('/user/login', methods=['POST'])
def login():
    errors = User.validate_login(request.form)
    if errors:
        return redirect(url_for('main.home'))
    user = User.get_by_email({"email": request.form['login_email']})
    if not user or not bcrypt.check_password_hash(user.password, request.form['login_password']): 
        error = "Invalid email or password"
        errors.append(error)
        flash(error, 'error')
        return redirect(url_for('main.home'))
    session['id'] = user.id
    return redirect(url_for('user.profile'))

@user_bp.route('/user/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@user_bp.route('/user/create', methods=['POST'])
def new_user():
    errors = User.validate_registration(request.form)
    if errors:
        return redirect(url_for('main.home'))
    password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': password
    }
    user_id = User.save(data)
    session['id'] = user_id
    return redirect(url_for('main.home'))

@user_bp.route('/user/profile')
def profile():
    if not 'id' in session:
        return redirect(url_for('main.home'))
    id = session['id']
    user = User.get_user({'id': id})
    return render_template('profile.html')

