from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])

    # ✅ Input validation
    if area <= 0 or bedrooms <= 0 or bathrooms <= 0:
        return render_template(
            "index.html",
            prediction="❌ Please enter valid positive values"
        )

    prediction = model.predict([[area, bedrooms, bathrooms]])
    price = round(prediction[0], 2)

    return render_template(
        "index.html",
        prediction=f"₹ {price}"
    )

if __name__ == "__main__":
    app.run(debug=True)