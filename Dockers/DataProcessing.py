# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:44:45 2020

@author: wasil
"""
import pandas as pd
from pymongo import MongoClient 
import csv

# Creating a client 
client = MongoClient("mongodb://localhost:27017/") 
  
# Creating a database name "database" 
database = client["Bank"] 
print("Database is created !!")

# Creating a collection name "collection" 
collection = database["Customer Transactions"]
print("Collection is created")

# To check if the database is created or not.
list_of_database = client.list_database_names() 
if "Bank" in list_of_database: 
	print("Exists !!") 
# To check if the collection is created.
list_of_collection = database.list_collection_names()
if "Customer Transaction" in list_of_collection:
    print("Exists !!")



dir_path = "D:/ML/Tutorials/Git/Dockers/Groceries with card.xlsx"
csv_file = "D:/ML/Tutorials/Git/Dockers/Groceries with card.csv"

data = pd.read_excel (dir_path)
data.set_index("SNo", inplace=True)
data.to_csv(csv_file)

header= [ "SNo", "Date", "Place","Item", "Amount", "Total"]
with open(csv_file, encoding='utf-8') as csvf:
    reader = csv.DictReader( csvf, header)
    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]
        # push the data into database.            
        database.CustomerTransactions.insert_one(row)

