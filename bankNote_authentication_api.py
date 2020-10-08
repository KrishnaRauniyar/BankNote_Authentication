from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

import pickle
Pickled_in = open('classifier_bankNote_authentication.pkl', 'rb')
classifier = pickle.load(Pickled_in)

# always provide a decorator to run the api
@app.route('/')
def home():
    return render_template('index.html')

# api through a post request i.e throgh a test file
@app.route('/predict', methods=["POST"])
def predict():
    """Let's Authenticate the Banks Note
    """
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The predicted value for your bank note is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
