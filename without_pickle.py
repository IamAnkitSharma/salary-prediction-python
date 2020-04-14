from flask import Flask,render_template,request,jsonify
import numpy
import pickle
import pandas
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('predict.html')


@app.route('/predict',methods=['POST'])
def predict():
    dataset = pandas.read_csv('salaryData.csv')
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
  
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 0)
    linearRegressor = LinearRegression()
    linearRegressor.fit(xTrain, yTrain)
    
    
    yPrediction = linearRegressor.predict(np.array([float(request.form['experience'])]).reshape(1,1))
    
    return "Salary Should be approximately - " +str(yPrediction[0])

@app.route('/predict',methods=['GET'])
def predictAPI():
    dataset = pandas.read_csv('salaryData.csv')
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
  
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 0)
    linearRegressor = LinearRegression()
    linearRegressor.fit(xTrain, yTrain)
    
    
    yPrediction = linearRegressor.predict(np.array([float(request.args['experience'])]).reshape(1,1))
    
    return jsonify({"result":str(yPrediction[0])})
if __name__ == '__main__':
   app.run(debug=True)