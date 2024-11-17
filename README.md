# California Housing Price Prediction API

This API is designed to solve a predictive modeling task that estimates housing prices in California based on various housing and demographic features. It leverages a pre-trained XGBoost model 
optimized to predict the Median House Value in different California census tracts. The model was trained on historical housing data and considers features like house age, average number of rooms,
population, and geographic information to make its predictions.

## Installation and Setup

1. Clone the Repository
2. Install Dependencies: Install the dependencies from requirements.txt
3. Place the Model File:
   Ensure the pre-trained model file xgboost_california_model.pkl is in the same directory as app.py

## Running the API
Start the Flask app by running:
```bash
python app.py
```

If successful, the server should run on http://127.0.0.1:5000, displaying:
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

   
