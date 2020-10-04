from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flask import render_template

app = Flask(__name__)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome all"

# GET method.
# Declaring variables values from the url bar/postman application.
@app.route('/predict', methods=["GET"])
def predict_note_authentication():
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy =  request.args.get("entropy")
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    
    return "The predicted value is: " + str(prediction)

# POST method. - This can be done by postman.
@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    
    return "The predicted value for csv is: " + str(list(prediction))

# Using html syntax
@app.route("/form", methods=["GET"])
def get_form():
    return render_template('index.html')
@app.route('/predict_html', methods=["POST"])
def predict_html():
    variance = request.form.get('variance')
    skewness = request.form.get('skewness')
    curtosis = request.form.get('curtosis')
    entropy = request.form.get('entropy')
    
    # Get the prediction.
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])    
    
    return "The predicted value is: " + str(list(prediction))

# Using html and uploading file there.
@app.route('/predict_html_file', methods=["GET", "POST"])
def predict_html_file():    
    if request.method == "POST":
        df_test = pd.read_csv(request.files.get("file")) 
        prediction = classifier.predict(df_test)        
        return "The predicted value for csv is: " + str(list(prediction))
    
if __name__ == '__main__':
    app.run()