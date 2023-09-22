
from flask import Flask, render_template, request
import os 
import numpy as np 
import pandas as pd 
from src.Mlflow_Project.pipeline.prediction import PredictionPipeline


app = Flask(__name__)

@app.route('/', methods=['GET'])  # route to display the home page 
def homepage():
    return render_template("index.html")



@app.route('/train', methods = ['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"


@app.route('/predict', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user 

            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulphur_dioxide = float(request.form['free_sulphur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulphur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))
        
        except Exception as e:
            print("The Exception message is: ", e)
            return "Something is wrong"
        
        else:
            return render_template("index.html")
        
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000, debug = True)



