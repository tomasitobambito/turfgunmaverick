import json
import os.path

class ManagerBase:
    def __init__(self, filePath):
        self.filePath = filePath

        if not os.path.exists(self.filePath):
            self.reset()


    def read_file(self):
        with open(self.filePath) as file:
            return json.load(file)
    

    def save_file(self, data):
        with open(self.filePath, 'w') as file:
            json.dump(data, file)


    def reset(self):
        defaultReset = {}

        self.save_file(defaultReset)