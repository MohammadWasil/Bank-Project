from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle
from pymongo import MongoClient 
import json

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
        #user_credentials = jsonify(request.form)
        user_signup_credentials = json.loads(json.dumps(request.form))
        first_name_reg = user_signup_credentials["first_name_reg"]
        last_name_reg = user_signup_credentials["last_name_reg"]
        username_reg = user_signup_credentials["username_reg"]
        password_reg = user_signup_credentials["password_reg"]
        
        document = { "first name" : first_name_reg, "last name" : last_name_reg, 
                    "username" : username_reg, "password" : password_reg}
        
        collection_username.insert_one(document)

        return render_template('register_page.html', registered = True)
    
    except Exception as register_username_exception:
        return jsonify({"Error:" : str(register_username_exception)} )

@app.route('/login_sucess', methods = ["POST"])
def login():
    
    try:
        user_login_credentials = json.loads(json.dumps(request.form))
        username = user_login_credentials["username"]
        password = user_login_credentials["password"]
        
        #username = user_login_credentials.get("username")
        #password = user_login_credentials.get("password")
        #print(username)

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
        return jsonify({"Error " : str(error)})

# transaction_hisory_page
@app.route('/transaction_history', methods=["GET"])
def transaction_history():
    try:
        row = collection_customer_transaction.find() 
        return render_template('transaction_history.html', documents=row)
    except Exception as e:
        return jsonify({"Error " : str(e)})
    
@app.route('/update_transaction', methods=["POST"])
def update_transaction():
    try:
        update_history = json.loads(json.dumps(request.form))
        
        SNo     = update_history["SNo"]
        date    = update_history["date"]
        place   = update_history["place"]
        item    = update_history["item"]
        amount  = update_history["amount"]
        total   = update_history["total"]
        
        document = {"SNo" : SNo, "Date" : date, "Place" : place, "Item" : item, "Amount" : amount, "Total" : total}

        collection_customer_transaction.insert_one(document)
        
        return render_template('logged_in.html')
    
    except Exception as update_error:
        return jsonify({"Error " : str(update_error)})
    
# Using html syntax
#@app.route("/form", methods=["GET"])
#def get_form():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)