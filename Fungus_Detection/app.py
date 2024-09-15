from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


app = Flask(__name__, template_folder='fungus/template')


log_model = pickle.load(open('fungus/models/log.pkl', 'rb'))
standard_scaler = pickle.load(open('fungus/models/scaler.pkl', 'rb'))
print(type(standard_scaler))

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
    if request.method == 'POST':
        try:
            temperature = float(request.form.get('Temperature'))
            humidity = float(request.form.get('Humidity'))
            co = float(request.form.get('CO'))
            nh3 = float(request.form.get('NH3'))
            c4h10 = float(request.form.get('C4H10'))
            ch4 = float(request.form.get('CH4'))
            light_intensity = float(request.form.get('LightIntensity'))

            # Prepare features as a 2D array
            features = [temperature, humidity, co, nh3, c4h10, ch4, light_intensity]
            features = np.array(features).reshape(1, -1)  # Reshape to 2D array
            features = standard_scaler.transform(features)

            result = log_model.predict(features)[0]

            return render_template('predict.html', result=result)
        except Exception as e:
            print(f"Error: {e}")
            return render_template('predict.html', result="Error occurred")
    
    return render_template('predict.html')

if __name__ == "__main__":
    app.run( )
