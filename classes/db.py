import os
from dotenv import load_dotenv
from pymongo import MongoClient
from random import choice

load_dotenv()

def DB(collectioName="Movie"):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = os.getenv("CONNECTION_STRING")
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   dbname = client["MongoMovieDB"]
   collection = dbname[collectioName]
   return collection
 
def Inject(object, db):
    try:
        db.insert_one(object)
    except:
        pass

def Update(object, db):
    try:
        db.update_one(object)
    except:
        pass



