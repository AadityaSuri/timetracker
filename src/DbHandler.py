from pymongo import MongoClient
import datetime
import time
from task import Task  

# create a mongodb handler class and connect to localhost

class DbHandler:

    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client["timetracker"]
        self.collection = self.db["tasks"]
        
    # for adding a new task to the database
    def StartTask(self, name, category):
        self.collection.insert_one({"name": name, "category": category, "start": datetime.datetime.now(), "end": None})

    # for stopping a task
    def StopTask(self, name):
        self.collection.update_one({"name": name}, {"$set": {"end": datetime.datetime.now()}})

    # for getting all tasks
    def GetRunningTasks(self):
        return self.collection.find({"end": None})
    

    

