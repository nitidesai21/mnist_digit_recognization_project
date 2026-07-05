from flask import Flask,render_template,request
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
app=Flask(__name__)
model=load_model("mnist_model.h5")
UPLOAD_FOLDER='uploads'
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def predict():
    file=request.files["image"]
    filepath=os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )
    file.save(filepath)
    img=cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(img,(28,28))
    img=img.astype("float32")/255.0
    img=img.flatten().reshape(1,784)
    prediction=model.predict(img,verbose=0)
    digit=np.argmax(prediction)
    confidence=np.max(prediction)*100
    return render_template(
        "index.html",
        prediction=digit,
        confidence=round(float(confidence),2)
    )
if __name__=="__main__":
    app.run(debug=True)
    