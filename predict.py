from flask import Flask
from flask import request
from flask import jsonify
import tensorflow as tf
import numpy as np

model_file = 'jellyfish.h5'

model = tf.keras.models.load_model(model_file)

app = Flask('potability')

@app.route('/predict', methods=['POST'])
def predict():
    parameters = request.get_json() # return a dict

    if parameters['url'] != '':
        print("URL passed")
    elif parameters['path'] != '':
        print("Local file used")

    

    return "OK"
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)