# Copyright 2018 Qinjin Jia qjia@bu.edu

# db.py 

" Import airport location data to Mongodb" 
JSON_FILE_NAME = "airports.json" 

# Connect to Mongodb server
from pymongo import MongoClient
client = MongoClient()

# Access the database 'airport_location'
db = client['airport_location']

# Import json file
import json
f = open(JSON_FILE_NAME, 'r') 
data = json.loads(f.read())

airports = db.posts.insert_many(data)
print("finish")


#mongo
#show dbs
#use airport_location
#show collections
#read: db.posts.find()
#search: db.posts.find({...})
#insert: db.posts.insertOne({...})
#update: db.posts.updateOne({...})
