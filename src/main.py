from DbHandler import DbHandler
from task import Task
import datetime
import time


# create a mongodb handler class and connect to localhost

DbHandler = DbHandler()

DbHandler.StartTask("test", "test")
DbHandler.StartTask("test2", "test2")

tasks = DbHandler.GetRunningTasks()

time.sleep(5)

DbHandler.StopTask("test")

tasks = DbHandler.GetRunningTasks()

# for getting all tasks

