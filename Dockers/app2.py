from flask import Flask, request
import pandas as pd
import pickle
from flask import render_template
from pymongo import MongoClient 

app = Flask(__name__)

# Creating a connection with the MongoDB database
client = MongoClient("mongodb://localhost:27017/") 
collection_customer_transaction = client.Bank.CustomerTransactions   # collection/table of customer transaction
collection_username = client.Bank.Usernames              # collection/table of customer transaction

@app.route('/')
def welcome():
    return render_template('index.html')

# Go to the register page
@app.route('/register_here_page')
def register_here_page():
    return render_template( 'register_page.html')
    
@app.route('/register_username', methods = ["POST"])
def register_users():
    try:
        first_name_reg = request.form["first_name_reg"]
        last_name_reg = request.form["last_name_reg"]
        username_reg = request.form["username_reg"]
        password_reg = request.form["password_reg"]
        
        document = { "first name" : first_name_reg, "last name" : last_name_reg, 
                    "username" : username_reg, "password" : password_reg}
        
        collection_username.insert_one(document)
        
        return render_template('register_page.html', registered = True)
    
    except Exception as register_username_exception:
        return "Error : " + str(register_username_exception)

@app.route('/login_sucess', methods = ["POST"])
def login():
    try:

        username = request.form["username"]
        password = request.form["password"]
        
        # Check if the user login and password are correct or not.
        query_username = { "username" : username}
        your_username = collection_username.find(query_username)
        
        for record in your_username:    
            if record["password"] == password:
                print("password is correct")
                return render_template('logged_in.html')
            else:
                print("The username and password that you entered is wrong!")
                return render_template("index.html", wrong_info = True)
    except Exception as error:
        return "Error : " + str(error)
    

# transaction_hisory_page
@app.route('/transaction_history', methods=["GET"])
def transaction_history():
    try:
        row = collection_customer_transaction.find() 
        return render_template('transaction_history.html', documents=row)
    except Exception as e:
        return "Error : " + str(e)
    
@app.route('/update_transaction', methods=["POST"])
def update_transaction():
    try:

        SNo = request.form["SNo"]
        date = request.form["date"]
        place = request.form["place"]
        item = request.form["item"]
        amount = request.form["amount"]
        total = request.form["total"]
        
        document = {"SNo" : SNo, "Date" : date, "Place" : place, "Item" : item, "Amount" : amount, "Total" : total}

        collection_customer_transaction.insert_one(document)
        
        return render_template('logged_in.html')
    
    except Exception as update_error:
        return "Error : " + str(update_error)
    
# Using html syntax
#@app.route("/form", methods=["GET"])
#def get_form():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run()