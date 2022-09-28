# -*- coding: utf-8 -*-
"""
@author: Salvador HS
"""
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in  = open("naive_bayes.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Please specify /apidocs on the URL to access the API"


@app.route('/predict',methods=["Get"])
def predict_virus():
    """White Spot Virus Detection
    Input data must be scaled using Robust Scaling

    Predictions are made by using a Bayes Classifier
    ---
    parameters:  
      - name: Area_ha
        in: query
        type: number
        required: true
      - name: SoilType
        in: query
        type: number
        required: true
      - name: PeriodOfFallow
        in: query
        type: number
        required: true
      - name: StockingDensity
        in: query
        type: number
        required: true
      - name: StockingAge_Days
        in: query
        type: number
        required: true
      - name: FeedType
        in: query
        type: number
        required: true
      - name: pH
        in: query
        type: number
        required: true
      - name: Salinity
        in: query
        type: number
        required: true
      - name: PreviousPrevalence
        in: query
        type: number
        required: true
      - name: CurrentPrevalance
        in: query
        type: number
        required: true
    responses:
        200:
            description: Predicted values
        
    """
    Area_ha            = request.args.get("Area_ha")
    SoilType           = request.args.get("SoilType")
    PeriodOfFallow     = request.args.get("PeriodOfFallow")
    StockingDensity    = request.args.get("StockingDensity")
    StockingAge_Days   = request.args.get("StockingAge_Days")
    FeedType           = request.args.get("FeedType")
    pH                 = request.args.get("pH")
    Salinity           = request.args.get("Salinity")
    PreviousPrevalence = request.args.get("PreviousPrevalence")
    CurrentPrevalance  = request.args.get("CurrentPrevalance")
    
    prediction         = classifier.predict([[float(Area_ha), float(SoilType), float(PeriodOfFallow), float(StockingDensity), float(StockingAge_Days), float(FeedType), float(pH), float(Salinity), float(PreviousPrevalence), float(CurrentPrevalance)]])
    print(prediction)
    return "The virus prediction is "+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_virus_file():
    """Please provide an Excel dataset 
    Input data must be scaled using Robust Scaling

    Formula: (X - Xmedian)/InterQuantileRange 
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_excel(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))


if __name__=='__main__':
    app.run(host='0.0.0.0',port = 8000)
    
    
    
