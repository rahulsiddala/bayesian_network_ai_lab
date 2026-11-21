from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .models import db, Patient, Measurement
from . import create_app
from statistics.bayesian_pipeline import predict_disease_probability

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    patients = Patient.query.all()
    return render_template('home.html', patients=patients)

@main_bp.route('/patient/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        # Create patient record
        patient = Patient(name=name, age=age, sex=sex)
        db.session.add(patient)
        db.session.commit()
        flash('Patient added successfully.', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_patient.html')

@main_bp.route('/patient/<int:patient_id>', methods=['GET', 'POST'])
def view_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    if request.method == 'POST':
        # Assume measurement fields posted
        data = {
            'age': patient.age,
            'sex': patient.sex,
            'cp': request.form.get('cp'),
            'trestbps': request.form.get('trestbps'),
            'chol': request.form.get('chol'),
            'fbs': request.form.get('fbs'),
            'restecg': request.form.get('restecg'),
            'thalach': request.form.get('thalach'),
            'exang': request.form.get('exang'),
            'oldpeak': request.form.get('oldpeak'),
            'slope': request.form.get('slope'),
            'ca': request.form.get('ca'),
            'thal': request.form.get('thal')
        }
        prob = predict_disease_probability(data)
        return render_template('patient_detail.html', patient=patient, probability=prob)
    return render_template('patient_detail.html', patient=patient)

@main_bp.route('/stats', methods=['GET'])
def stats_dashboard():
    # Placeholder for statistical analysis UI
    return render_template('stats_dashboard.html')
