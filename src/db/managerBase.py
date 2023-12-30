import json
import os.path

class ManagerBase:
    """Base DB manager class that other DB managers inherit from.
    """
    def __init__(self, filePath):
        self.filePath = filePath

        if not os.path.exists(self.filePath):
            self.reset()


    def read_file(self):
        """Default read file method that returns file contents as a dict.

        Returns:
            dict: Dictionary containing the json files contents.
        """
        with open(self.filePath) as file:
            return json.load(file)
    

    def save_file(self, data):
        """Default save file method that saves whatever data it was given as a json file.

        Args:
            data (dict or List(dict)): data to be saved. Must be given as a dict or list of dicts. 
        """
        with open(self.filePath, 'w') as file:
            json.dump(data, file)


    def reset(self):
        """Default reset method, unused but here for backup. Will write an empty json file.
        """
        defaultReset = {}

        self.save_file(defaultReset)