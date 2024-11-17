# California Housing Price Prediction API

This API is designed to solve a predictive modeling task that estimates Housing Values in California (19990) based on various housing and demographic features. It leverages a pre-trained XGBoost model 
optimized to predict the Median House Value in different California census tracts. The model was trained on historical housing data and considers features like house age, average number of rooms,
population, and geographic information to make its predictions.

This API is built using Python 3.12 and utilizes Flask for handling HTTP requests, with the housing price prediction model implemented using XGBoost.

## Installation and Setup

1. Clone the Repository
2. Install Dependencies:
   Install the dependencies from requirements.txt
4. Place the Model File:
   Ensure the pre-trained model file xgboost_california_model.pkl is in the same directory as app.py

## Running the API
Start the Flask app by running:
```bash
python app.py
```

If successful, the server should run on http://127.0.0.1:5000, displaying:
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

   
## API Usage
- Endpoint Details
- URL: /predict
- Method: POST
- Content-Type: application/json

## Example Input
Submit JSON data with the following fields:
```bash
{
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.023,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23,
    "IncomeCategory": 5
}

```
## Example Output
A successful response provides a predicted housing price:

```bash
{
  "prediction": 2.42
}

```

## Testing the API

### Using curl
To test with curl, run:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.023810,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23,
    "IncomeCategory": 5
}'

```
### Using Postman
1. Open Postman.
2. Create a new request with method POST.
3. Set the URL to http://127.0.0.1:5000/predict.
4. Under Body, select raw and choose JSON format.
5. Paste the example input JSON.
6. Click Send.

## Stopping the API
To stop the API, press CTRL+C in the terminal.



