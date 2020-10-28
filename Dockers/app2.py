from flask import Flask, request
import pandas as pd
import pickle
from flask import render_template
from pymongo import MongoClient 


app = Flask(__name__)

# Creating a connection with the MongoDB database
client = MongoClient("mongodb://localhost:27017/") 
collection_customer_transaction = client.Bank.CustomerTransactions

@app.route('/')
def welcome():
    return render_template('index.html')


# Go to the register page
@app.route('/register_here_page')
def register_here_page():
    return render_template( 'register_page.html')
    
@app.route('/register_username', methods = ["GET"])
def register_users():
    username = request.form["username_reg"]
    password = request.form["password_reg"]
    
    return username, password

# transaction_hisory_page
@app.route('/transaction_history', methods=["GET"])
def transaction_history():
    try:
        row = collection_customer_transaction.find() 
        return render_template('transaction_history.html', documents=row)
    except Exception as e:
        return "Error 404" + str(e)
    




# Using html syntax
#@app.route("/form", methods=["GET"])
#def get_form():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run()