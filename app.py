import flask
import numpy as np
import json
import pickle
from flask import Flask, jsonify, request


app = Flask(__name__)

def load_model():
    """
    loads model from saved pickle file
    parameters: None
    output: model

     """
    file_name = "model_file.pkl"
    with open(file_name, 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    return model


def __process_input(request_data:str) -> np.array:
    """
    processes request input as a json array and asserts the shape and length of array
    parameters: request_data 
    output: array
    """
    input_array = np.asarray(json.loads(request_data)["inputs"])
    assert len(input_array.shape) == 2, "inputs must be a 2-D array"
    assert input_array.shape[1] == 13, "values for each of 13 features need to be specified"
    return input_array

@app.route('/',methods=['GET'])
def home():
    """
    returns an output for a GET and '/' route
    parameters: None
    output: statement
    """
    return 'House Price Prediction - Add a "/predict" and POST request with input parameters to make a price prediction.'


@app.route('/predict', methods=['POST'])
def predict() -> str:
    """
    returns a prediction for POST and input parameters
    parameters: None
    output: json
    """
    try:
        input_params = __process_input(request.data)
        model = load_model()
        predictions = model.predict(input_params)
        return json.dumps({"Predicted price": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
