from . import db

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Additional fields as needed

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(1), nullable=False)  # 'M' or 'F'
    # Relationship to measurements
    measurements = db.relationship('Measurement', backref='patient', lazy=True)

class Measurement(db.Model):
    __tablename__ = 'measurements'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    cp = db.Column(db.Integer)          # chest pain type
    trestbps = db.Column(db.Integer)    # resting blood pressure
    chol = db.Column(db.Integer)        # serum cholesterol
    fbs = db.Column(db.Integer)         # fasting blood sugar > 120 mg/dl
    restecg = db.Column(db.Integer)    # resting electrocardiographic results
    thalach = db.Column(db.Integer)    # maximum heart rate achieved
    exang = db.Column(db.Integer)      # exercise induced angina
    oldpeak = db.Column(db.Float)      # ST depression induced by exercise
    slope = db.Column(db.Integer)      # slope of the peak exercise ST segment
    ca = db.Column(db.Integer)         # number of major vessels (0-3) colored by fluoroscopy
    thal = db.Column(db.Integer)       # thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
