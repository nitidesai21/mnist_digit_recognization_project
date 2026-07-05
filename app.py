from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

model = load_model("mnist_model.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return render_template("index.html", prediction="No image", confidence=0)

    file = request.files["image"]

    if file.filename == "":
        return render_template("index.html", prediction="No image", confidence=0)

    file_bytes = np.frombuffer(file.read(), np.uint8)

    img_color = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    img_gray = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    img_gray = cv2.resize(img_gray, (28, 28))
    img_gray = img_gray.astype("float32") / 255.0
    img_gray = img_gray.flatten().reshape(1, 784)

    result = model.predict(img_gray, verbose=0)
    digit = np.argmax(result)
    confidence = round(np.max(result) * 100, 2)

    return render_template(
        "index.html",
        prediction=digit,
        confidence=confidence
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)