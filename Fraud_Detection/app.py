from flask import Flask, request, jsonify , render_template
import pandas as pd
import pickle

import numpy as np

app = Flask(__name__)

kmeans_model = pickle.load(open('model/kmeans_model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    amount = float(request.form["Amount"])
    hour = int(request.form["Hour"])
    distance = float(request.form["Distance_km"])
    device_score = int(request.form["Device_Score"])
    daily_transactions = int(request.form["Daily_Transactions"])
    failed_logins = int(request.form["Failed_Logins"])
    international = int(request.form["International"])
    weekend = int(request.form["Weekend"])
    account_age = int(request.form["Account_Age_Months"])

    data = pd.DataFrame({
        "Amount": [amount],
        "Hour": [hour],
        "Distance_km": [distance],
        "Device_Score": [device_score],
        "Daily_Transactions": [daily_transactions],
        "Failed_Logins": [failed_logins],
        "International": [international],
        "Weekend": [weekend],
        "Account_Age_Months": [account_age]
    })

    data_scaled = scaler.transform(data)
    cluster = kmeans_model.predict(data_scaled)[0]


    if cluster == 1:
        prediction = " Fraudulent Transaction Detected"
    else:
        prediction = " Genuine Transaction"

    return render_template("result.html", prediction=prediction)



if __name__ == '__main__':
    app.run(debug=True)