import numpy as np
#from flask import Flask, request, jsonify, render_template
from flask import Flask
from flask import render_template 
from flask import Response
from flask import request
from flask import jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('Model_RandomForestRegressor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    temp_array = list()
    
    KM_Driven = int(request.form['KM_Driven'])
    Years_Old = int(request.form['Years_Old'])
    
    temp_array = temp_array + [KM_Driven, Years_Old]

    Brand_Type = request.form['Brand-Type']
    if Brand_Type == 'Audi':
        temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0]
    elif Brand_Type == 'BMW':
        temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0]
    elif Brand_Type == 'Honda':
        temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0]
    elif Brand_Type == 'Hyundai':
        temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0]
    elif Brand_Type == 'JLR':
        temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0]
    elif Brand_Type == 'Mahindra':
        temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0]
    elif Brand_Type == 'Maruti':
        temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0]
    elif Brand_Type == 'Mercedes':
        temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0]
    elif Brand_Type == 'Tata':
        temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0]
    elif Brand_Type == 'Toyota':
        temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0]
    elif Brand_Type == 'Volkswagen':
        temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1]

    Fuel_Type = request.form['Fuel-Type']
    if Fuel_Type == 'CNG':
        temp_array = temp_array + [1,0,0,0,0]
    elif Fuel_Type == 'Diesel':
        temp_array = temp_array + [0,1,0,0,0]
    elif Fuel_Type == 'Electric':
        temp_array = temp_array + [0,0,1,0,0]
    elif Fuel_Type == 'LPG':
        temp_array = temp_array + [0,0,0,1,0]
    elif Fuel_Type == 'Petrol':
        temp_array = temp_array + [0,0,0,0,1]
    
    Seller_Type = request.form['Seller-Type']
    if Seller_Type == 'Dealer':
        temp_array = temp_array + [1,0,0]
    elif Seller_Type == 'Individual':
        temp_array = temp_array + [0,1,0]
    elif Seller_Type == 'TrustMarkDealer':
        temp_array = temp_array + [0,0,1]
    
    Transmission_Type = request.form['Transmission-Type']
    if Transmission_Type == 'Automatic':
        temp_array = temp_array + [1,0]
    elif Transmission_Type == 'Manual':
        temp_array = temp_array + [0,1]
    
    Owner_Type = request.form['Owner-Type']
    if Owner_Type == 'First-Owner':
        temp_array = temp_array + [1,0,0,0,0]
    elif Owner_Type == 'Fourth-Above-Owner':
        temp_array = temp_array + [0,1,0,0,0]
    elif Owner_Type == 'Second-Owner':
        temp_array = temp_array + [0,0,1,0,0]
    elif Owner_Type == 'Test-Owner':
        temp_array = temp_array + [0,0,0,1,0]
    elif Owner_Type == 'Third-Owner':
        temp_array = temp_array + [0,0,0,0,1]

    data = np.array([temp_array])

    prediction = model.predict(data)
    output = round(prediction[0], 2)
    
    return render_template('index.html',prediction_text='Car selling price should be - RS {}'.format(output))

if __name__ == '__main__':
	app.run(debug=True)

