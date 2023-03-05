from DbHandler import DbHandler
from task import Task
import datetime
import time


# create a mongodb handler class and connect to localhost
DbHandler = DbHandler()


if __name__ == "__main__":
    print('start')

    # for adding a new task to the database
    t1 = Task("task1", "category1")
    DbHandler.StartTask(t1)

    print("current tasks")

    # print the entire tasks collection
    for t in DbHandler.collection.find():
        print(t)
    

