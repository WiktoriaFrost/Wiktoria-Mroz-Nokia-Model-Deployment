from flask import Flask, request, jsonify
import joblib
import numpy as np
import xgboost
import sklearn

app = Flask(__name__)

try:
    model = joblib.load('xgboost_california_model.pkl')
    print("Model successfully loaded.")
except Exception as e:
    print(f"Error loading model: {e}")


@app.route('/predict', methods=['POST'])
def predict():
    print(request)
    if request.is_json:

        data = request.get_json()

        features = [
            data.get('HouseAge'),
            data.get('AveRooms'),
            data.get('AveBedrms'),
            data.get('Population'),
            data.get('AveOccup'),
            data.get('Latitude'),
            data.get('Longitude'),
            data.get('IncomeCategory')
        ]

        if None in features:
            return jsonify({'error': 'Missing features in input'}), 400

        features = np.array(features).reshape(1, -1)

        try:
            prediction = model.predict(features)
            return jsonify({'prediction': float(prediction[0])})
        except Exception as e:
            return jsonify({'error': f"Prediction failed: {e}"}), 500
    else:
        return jsonify({'error': 'Request must be JSON'}), 400


if __name__ == '__main__':
    app.run(debug=False)


