from __future__ import division, print_function
import os
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH ='model_inception.h5'

model = load_model(MODEL_PATH)


def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x=x/255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds="Bacterial_spot"
    elif preds==1:
        preds="Early_blight"
    elif preds==2:
        preds="Late_blight"
    elif preds==3:
        preds="Leaf_Mold"
    elif preds==4:
        preds="Septoria_leaf_spot"
    elif preds==5:
        preds="Spider_mites Two-spotted_spider_mite"
    elif preds==6:
        preds="Target_Spot"
    elif preds==7:
        preds="Tomato_Yellow_Leaf_Curl_Virus"
    elif preds==8:
        preds="Tomato_mosaic_virus"
    else:
        preds="Healthy"

    return preds



@app.route('/predict', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename("image.jpg"))
            file.save(file_path)

            preds = model_predict(file_path, model)
            result = preds
            return  jsonify({"class": result})
        except Exception as e:
            return jsonify({"error": str(e)})
    
    return "OK"


if __name__ == '__main__':
    app.run()
