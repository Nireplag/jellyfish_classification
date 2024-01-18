from flask import Flask
from flask import request
from flask import jsonify
import tensorflow as tf
import numpy as np
import requests

model_file = 'jellyfish.h5'

model = tf.keras.models.load_model(model_file)

app = Flask('potability')

@app.route('/predict', methods=['POST'])
def predict():
    parameters = request.get_json() # return a dict

    if parameters['url'] != '':
        print("URL passed")
        img_data = requests.get(parameters['url']).content
        with open('image_name.jpg', 'wb') as handler:
          handler.write(img_data)
    elif parameters['path'] != '':
        print("Local file used")
        img_data = tf.keras.preprocessing.image.load_img(
              parameters['path'] , target_size=(179, 179)
              )
        x = np.array(img_data)
        img_data = np.array([x])


    pred = model.predict(img_data)

    classes = ['Moon_jellyfish', 'barrel_jellyfish',
                'blue_jellyfish', 'compass_jellyfish',
                'lions_mane_jellyfish', 'mauve_stinger_jellyfish']
    
    response = dict(zip(classes, pred[0]))
    jellyfish = max(response, key=response.get)


    result = {
        "payload": parameters,
        "jellyfish": jellyfish
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)