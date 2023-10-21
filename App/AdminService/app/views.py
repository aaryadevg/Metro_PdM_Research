# app/views.py

from flask import render_template, flash, redirect, url_for
from app import app, db, login_manager
from app.models import Admin
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm, SignupForm

@app.route('/')
@login_required
def index():
    return "Welcome"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign Up', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = SignupForm()
    
    if form.validate_on_submit():
        user = Admin(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User Created')
        return redirect(url_for('login'))
    
    return render_template('signup.html', title='Sign Up', form=form)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))
