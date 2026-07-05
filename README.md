# 🖊️ Handwritten Digit Recognition using Deep Learning (CNN)

A deep learning-based **Handwritten Digit Recognition** system that predicts handwritten digits (0–9) using a **Convolutional Neural Network (CNN)**. The project includes a trained model, a Flask web application, and a simple user-friendly interface where users can draw or upload a digit image for prediction.

---

## 📌 Project Overview

This project classifies handwritten digits by preprocessing the input image and feeding it into a trained CNN model.

The trained model is integrated into a **Flask web application**, allowing users to draw a digit on a canvas or upload an image and instantly receive the predicted digit.

---

## 🚀 Features

- ✍️ Draw handwritten digits on a digital canvas
- 📤 Upload handwritten digit images
- 🧠 CNN-based digit recognition
- ⚡ Real-time digit prediction
- 🌐 Simple Flask web interface
- 💾 Pre-trained model included

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Flask
- OpenCV
- NumPy
- Pillow (PIL)
- HTML
- CSS
- JavaScript

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/nitidesai21/mnist_digit_recognization_project.git
```

```bash
cd mnist_digit_recognization_project
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📊 Model Information

**Model:** Convolutional Neural Network (CNN)

**Dataset:** MNIST Handwritten Digit Dataset

**Input:** 28 × 28 grayscale image

**Output:** Predicted digit (0–9)

The model preprocesses the input image and predicts the corresponding handwritten digit.

---

## 🎯 Supported Classes

The model can recognize the following digits:

- 0️⃣ Zero
- 1️⃣ One
- 2️⃣ Two
- 3️⃣ Three
- 4️⃣ Four
- 5️⃣ Five
- 6️⃣ Six
- 7️⃣ Seven
- 8️⃣ Eight
- 9️⃣ Nine

---
## 📈 Future Improvements

- Webcam-based digit recognition
- Confidence score visualization
- Improved UI/UX
- Mobile-friendly interface
- Deploy on Render or Hugging Face Spaces

---
