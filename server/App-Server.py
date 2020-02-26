import numpy as np
import io
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_model():
    global model
    global graph
    model = load_model('../model/SmartBin-Model.h5', compile=False)    
    graph = tf.get_default_graph()

def ToClass(image):
    if image.shape[-1] > 1:
        return image.argmax(axis=-1)
    else:
        return (image > 0.5).astype('int32')
def ResultClass(R):
    if(ToClass(R)==0):
        return("B")
    else:
        return("G")

def prepare_image(image, target):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/")
def home():
    return ("<h1>Welcome to Smart-Bin Server</h1>")

@app.route("/predict", methods=["POST"])
def predict():
    if request.files.get("image"):
        image = request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        image = prepare_image(image, target=(224, 224))
        with graph.as_default(): 
            preds = model.predict(image)         
    
    return jsonify(typebin = ResultClass(preds))

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    get_model()
    app.run(host='0.0.0.0',debug=True)