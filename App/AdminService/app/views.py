# app/views.py

from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db, login_manager
from app.models import Admin, SensorData
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm, SignupForm
import requests

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

@app.route('/sensor_data', methods=['POST'])
def create_sensor_data():
    sensor_data = request.get_json()
    
    processed_data = list(map(float, sensor_data.values()))
    
    r = requests.post("http://127.0.0.1:8000/Model", json=processed_data)
    if r.status_code != 200:
        return
    
    resp = r.json()
    
    
    # Create a new SensorData object from the JSON data
    sensor_data_obj = SensorData(
        TP2=sensor_data['TP2'],
        TP3=sensor_data['TP3'],
        H1=sensor_data['H1'],
        DV_pressure=sensor_data['DV_pressure'],
        Reservoirs=sensor_data['Reservoirs'],
        Oil_temperature=sensor_data['Oil_temperature'],
        Flowmeter=sensor_data['Flowmeter'],
        Motor_current=sensor_data['Motor_current'],
        COMP=sensor_data['COMP'],
        DV_eletric=sensor_data['DV_eletric'],
        Towers=sensor_data['Towers'],
        MPG=sensor_data['MPG'],
        LPS=sensor_data['LPS'],
        Oil_level=sensor_data['Oil_level'],
        Caudal_impulses=sensor_data['Caudal_impulses'],
        gpsSpeed=sensor_data['gpsSpeed'],
        pred_label = resp['predicted_label'],
        pred_class = resp['predicted_class'],
        confidence = resp['confidence']
    )
    
    # # Add the new SensorData object to the database
    db.session.add(sensor_data_obj)
    db.session.commit()

    # # Return a JSON response indicating that the sensor data was created successfully
    return jsonify({'message': 'Sensor data created successfully!'})
