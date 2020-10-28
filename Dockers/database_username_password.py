# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:46:08 2020

@author: wasil
"""
from pymongo import MongoClient 


client = MongoClient("mongodb://localhost:27017/") 


# Creating a collection name "collection" 
collection = client.Bank["Usernames"]
print("Collection Username is created")

# Now we need to inject the values into the collection username.