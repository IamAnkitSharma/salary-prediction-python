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

    filename = 'salary_prediction_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    val = loaded_model.predict(np.array([float(request.form['experience'])]).reshape(1,1))
    return render_template('predict.html',result='Salary - ₹ ' +str(val[0])+ ' /-',input=request.form['experience'])
    

@app.route('/predict',methods=['GET'])
def predictAPI():
    filename = 'salary_prediction_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    val = loaded_model.predict(np.array([float(request.args['experience'])]).reshape(1,1))
    
    
    
    return jsonify({"result":str(val[0])})
if __name__ == '__main__':
   app.run(debug=True)