import datetime

class Task:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.start = None
        self.end = None

    # def start_task(self):
    #     self.start = datetime.now()
    #     self.is_running = True

    # def stop_task(self):
    #     self.end = datetime.now()
    #     self.is_running = False
    
    # def get_timestamps(self):
    #     return (self.start, self.end)
    
    # def get_name(self):
    #     return self.name
    
    # def get_category(self):
    #     return self.category
    
    # def is_running(self):
    #     return self.status
    
    # def get_duration(self):
    #     if self.start and self.end:
    #         return self.end - self.start
    #     else:
    #         return None
    
    # def __str__(self):
    #     return self.name
    
    # def __repr__(self):
    #     return self.name
    
