from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import pickle
import numpy as np

crop_scaler = pickle.load(open('model/Crop_recom_scaler.pkl', 'rb'))
crop_model = pickle.load(open('model/Crop_recom_model.pkl', 'rb'))
crop_encoder = pickle.load(open('model/Crop_recom_encoder.pkl', 'rb'))

fertilizer_model = pickle.load(open('model/fertilizer_model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))
le_soil = pickle.load(open('model/le_soil.pkl', 'rb'))
le_crop = pickle.load(open('model/le_crop.pkl', 'rb'))
le_target = pickle.load(open('model/le_target.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/crop_recommendation")
def crop_recommendation():
    return render_template("crop.html")

@app.route("/fertilizer_recommendation")
def fertilizer_recommendation():
    return render_template("fertilizer.html")

@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

@app.route("/predict_crop", methods=["POST"])
def predict_crop():

    input_data = [[
        float(request.form['N']),
        float(request.form['P']),
        float(request.form['K']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]]

    # Scale input
    input_data_scaled = crop_scaler.transform(input_data)

    # Predict
    prediction = crop_model.predict(input_data_scaled)

    # Decode prediction
    predicted_crop = crop_encoder.inverse_transform(prediction)[0]

    return render_template("result.html", crop=predicted_crop)


@app.route("/fertilizer_predict", methods=["POST"])
def fertilizer_predict():

    temperature = float(request.form["temperature"])
    moisture = float(request.form["moisture"])
    rainfall = float(request.form["rainfall"])
    ph = float(request.form["ph"])
    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    carbon = float(request.form["carbon"])

    soil = request.form["soil"]
    crop = request.form["crop"]

    # Encode categorical values
    soil = le_soil.transform([soil])[0]
    crop = le_crop.transform([crop])[0]

    # Create input
    features = [[
        temperature,
        moisture,
        rainfall,
        ph,
        nitrogen,
        phosphorus,
        potassium,
        carbon,
        soil,
        crop
    ]]

    # Scale features
    features = scaler.transform(features)

    # Predict
    prediction = fertilizer_model.predict(features)

    # Decode prediction
    fertilizer = le_target.inverse_transform(prediction)[0]

    return render_template(
        "result.html",
        fertilizer=fertilizer
    )

if __name__ == '__main__':
    app.run(debug=True)