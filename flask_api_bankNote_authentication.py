from flask import Flask, request
import pandas as pd
import numpy as np

### For the UI section we will use flasgger
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

import pickle
Pickled_in = open('classifier_bankNote_authentication.pkl', 'rb')
classifier = pickle.load(Pickled_in)

# always provide a decorator to run the api
@app.route('/')
def welcome():
    return "Welcome All"

# In the data we have 4 features
# api through a get request (http://127.0.0.1:5000/predict?variance=0&skewness=-2&curtosis=-2&entropy=-1)
@app.route('/predict')
def predict_note_authentication():
    """Let's Authenticate the bank notes
    This is using docstring for specification
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
          200:
              description: The output values
    """

    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "The prediction is: " + str(prediction)


# api through a post request i.e throgh a test file
@app.route('/predict_file', methods=["POST"])
def predict_note_files():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    df_test = pd.read_csv(request.files.get('file'))
    print(df_test.head())
    prediction = classifier.predict(df_test)
    return "The predicted values are: " + str(list(prediction))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)