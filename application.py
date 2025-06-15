from flask import Flask,request, jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Load the pre-trained model
riding_model = pickle.load(open('model/ridge_regression_model.pkl', 'rb'))
standard_scaler = pickle.load(open('model/scaler.pkl', 'rb'))
application = Flask(__name__)
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
            Temperature=float(request.form.get('Temperature'))
            RH=float(request.form.get('RH'))
            Ws=float(request.form.get('Ws'))
            Rain=float(request.form.get('Rain'))
            FFMC=float(request.form.get('FFMC'))
            DMC=float(request.form.get('DMC'))
            ISI=float(request.form.get('ISI'))
            Classes=float(request.form.get('Classes'))
            Region=float(request.form.get('Region'))

            new_data_scaled=standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

            result=riding_model.predict(new_data_scaled)
            return render_template('app.html', results=result[0])
    else:
        return render_template('app.html')
        # Get form data
        # Convert categorical variables to numeric

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)