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
client_atlas = MongoClient("MONGO_CONNECTION_STRING") 

  
# Creating a database name "database" 
database = client["Bank"] 
print("Database is created !!")

# Creating a collection name "collection" 
collection = database["CustomerTransactions"]
print("Collection is created")

# Creating a database name "database" 
database_atlas = client_atlas["Bank"] 
print("Database is created !!")

# Creating a collection name "collection" 
collection_atlas = database_atlas["CustomerTransactions"]
print("Collection is created")

# To check if the database is created or not.
print("Checking for local database:")
list_of_database = client.list_database_names() 
if "Bank" in list_of_database: 
	print("Database bank Exists !!") 
# To check if the collection is created.
list_of_collection = database.list_collection_names()
if "CustomerTransaction" in list_of_collection:
    print("database customerTransaction Exists !!")

print("Checking for cloud database:")
list_of_database = client_atlas.list_database_names() 
if "Bank" in list_of_database: 
	print("Database bank Exists !!") 
# To check if the collection is created.
list_of_collection = database_atlas.list_collection_names()
if "CustomerTransaction" in list_of_collection:
    print("database customerTransaction Exists !!")



dir_path = "D:/ML/Tutorials/Git/Bank/Groceries with card.xlsx"
csv_file = "D:/ML/Tutorials/Git/Bank/Groceries with card.csv"

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
        database_atlas.CustomerTransactions.insert_one(row)
        
