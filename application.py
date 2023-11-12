from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)
app=application

scaler=pickle.load(open("Model/standardScalar.pkl", "rb"))
model = pickle.load(open("Model/model2.pkl", "rb"))

## Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""


    if request.method=='POST':

        GamesPlayed=int(request.form.get("GamesPlayed"))
        MinutesPlayed = float(request.form.get('MinutesPlayed'))
        PointsPerGame = float(request.form.get('PointsPerGame'))
        FieldGoalsMade = float(request.form.get('FieldGoalsMade'))
        FieldGoalAttempts = float(request.form.get('FieldGoalAttempts'))
        FieldGoalPercent = float(request.form.get('FieldGoalPercent'))
        PointMade = float(request.form.get('PointMade'))
        PointAttempt = float(request.form.get('PointAttempt'))
        PointPercent=float(request.form.get('PointAttempt'))
        FreeThrowMade=float(request.form.get('FreeThrowMade'))
        FreeThrowAttempts=float(request.form.get('FreeThrowAttempts'))
        FreeThrowPercent=float(request.form.get('FreeThrowPercent'))
        OffensiveRebounds=float(request.form.get('OffensiveRebounds'))
        DefensiveRebounds=float(request.form.get('DefensiveRebounds'))
        Rebounds=float(request.form.get('Rebounds'))
        Assists=float(request.form.get('Assists'))
        Steals=float(request.form.get('Steals'))
        Blocks=float(request.form.get('Blocks'))
        Turnovers=float(request.form.get('Turnovers'))

        new_data=scaler.transform([[GamesPlayed,MinutesPlayed,PointsPerGame,FieldGoalsMade,FieldGoalAttempts,FieldGoalPercent,PointMade,PointAttempt,PointPercent,FreeThrowMade,FreeThrowAttempts,FreeThrowPercent,OffensiveRebounds,DefensiveRebounds,Rebounds,Assists,Steals,Blocks,Turnovers]])
        predict=model.predict(new_data)
        
        if predict[0] ==1 :
            result = 'One'
        else:
            result ='Zero'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")