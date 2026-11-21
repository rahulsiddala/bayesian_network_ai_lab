from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)])
    sex = SelectField('Sex', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Add Patient')

class MeasurementForm(FlaskForm):
    cp = SelectField('Chest Pain Type', choices=[('0', 'Typical Angina'), ('1', 'Atypical Angina'), ('2', 'Non-anginal Pain'), ('3', 'Asymptomatic')], validators=[DataRequired()])
    trestbps = IntegerField('Resting Blood Pressure', validators=[DataRequired(), NumberRange(min=0)])
    chol = IntegerField('Serum Cholesterol', validators=[DataRequired(), NumberRange(min=0)])
    fbs = SelectField('Fasting Blood Sugar > 120 mg/dl', choices=[('0', 'False'), ('1', 'True')], validators=[DataRequired()])
    restecg = SelectField('Resting ECG', choices=[('0', 'Normal'), ('1', 'ST-T Wave Abnormality'), ('2', 'Left Ventricular Hypertrophy')], validators=[DataRequired()])
    thalach = IntegerField('Maximum Heart Rate Achieved', validators=[DataRequired(), NumberRange(min=0)])
    exang = SelectField('Exercise Induced Angina', choices=[('0', 'No'), ('1', 'Yes')], validators=[DataRequired()])
    oldpeak = IntegerField('ST Depression', validators=[DataRequired()])
    slope = SelectField('Slope of Peak Exercise ST Segment', choices=[('0', 'Upsloping'), ('1', 'Flat'), ('2', 'Downsloping')], validators=[DataRequired()])
    ca = SelectField('Number of Major Vessels (0-3)', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], validators=[DataRequired()])
    thal = SelectField('Thalassemia', choices=[('3', 'Normal'), ('6', 'Fixed Defect'), ('7', 'Reversible Defect')], validators=[DataRequired()])
    submit = SubmitField('Submit Measurement')
