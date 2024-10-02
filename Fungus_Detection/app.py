import os
from flask import Flask, request, render_template, jsonify, redirect, url_for, flash
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from twilio.rest import Client  # For SMS
import requests  # To send requests to the Kindwise API
import base64

app = Flask(__name__, template_folder='fungus/template')

# Load model and scaler
log_model = pickle.load(open('fungus/models/log.pkl', 'rb'))
standard_scaler = pickle.load(open('fungus/models/scaler.pkl', 'rb'))

# Twilio credentials
# TWILIO_ACCOUNT_SID = ' # Your Twilio Account SID '
# TWILIO_AUTH_TOKEN = '# Your Twilio Auth Token'     
# TWILIO_PHONE_NUMBER = '# Replace with your Twilio phone number'  

def send_sms_alert(user_phone, message):
    """Function to send SMS alerts using Twilio."""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=user_phone,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

def get_user_details():
    """Function to manually retrieve user details."""
    return {
        'phone': '+917428428237',  # Replace with the actual phone number
    }

def get_recommendation(humidity, temperature):
    """Provide recommendations based on humidity and temperature."""
    recommendations = {
        'high_humidity': 'Reduce humidity by using a dehumidifier.',
        'low_ventilation': 'Increase airflow by opening windows or using fans.',
        'fungicide_suggestion': 'Consider using fungicides like copper sulfate.'
    }

    if humidity > 80:  # Adjust thresholds as needed
        return recommendations['high_humidity']
    elif temperature < 20:
        return recommendations['low_ventilation']
    else:
        return 'Conditions are optimal. No action needed.'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/read_more')
def read_more():
    return render_template('read_more.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    """Endpoint for predicting fungus based on sensor data."""
    if request.method == 'POST':
        try:
            user_details = get_user_details()
            temperature = float(request.form.get('Temperature'))
            humidity = float(request.form.get('Humidity'))
            co = float(request.form.get('CO'))
            nh3 = float(request.form.get('NH3'))
            c4h10 = float(request.form.get('C4H10'))
            ch4 = float(request.form.get('CH4'))
            light_intensity = float(request.form.get('LightIntensity'))

            features = [temperature, humidity, co, nh3, c4h10, ch4, light_intensity]
            features = np.array(features).reshape(1, -1)  # Reshape to 2D array
            features = standard_scaler.transform(features)

            result = log_model.predict(features)[0]
            if result == 1:
                send_sms_alert(user_details['phone'], 'Alert: Fungus detected in the air! Take immediate action.')
                result_text = "Fungus detected! High risk."
            else:
                result_text = "No fungus detected. Everything is fine."
            
            recommendation = get_recommendation(humidity, temperature)
            
            return render_template('predict.html', result=result_text, recommendation=recommendation)
        except Exception as e:
            print(f"Error: {e}")
            return render_template('predict.html', result="Error occurred")

    return render_template('predict.html')

@app.route('/identify_fungus', methods=['GET', 'POST'])
def identify_fungus():
    """Endpoint for identifying fungus through an uploaded image."""
    if request.method == 'POST':
        if 'fungusImage' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['fungusImage']

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        try:
            # Prepare the API request to Kindwise Mushroom API
            api_url = "https://mushroom.kindwise.com/api/v1/identify"
            headers = {
                'Authorization': ' # Your API key', 
            }
            # Convert the image to base64 to match Kindwise API requirements (if needed)
            image_base64 = base64.b64encode(file.read()).decode('utf-8')

            payload = {
                "images": [image_base64],  # base64 encoded image list
                "similar_images": True
            }

            response = requests.post(api_url, headers=headers, json=payload)

            if response.status_code == 200:
                return jsonify(response.json())
            else:
                return jsonify({"error": "Identification failed", "details": response.json()}), response.status_code
        except requests.exceptions.RequestException as e:
            s
            return jsonify({"error": "An error occurred while calling the API", "details": str(e)}), 500

    return render_template('identify_fungus.html')

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=True for better error handling during development
