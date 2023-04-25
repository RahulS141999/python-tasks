#module for loading data of json file
import json
import os

class JSONLoader:
    def __init__(self, file_path):
        
        self.file_path = file_path
        

    def load_json(self):
        file_path = os.path.join(os.path.dirname(__file__), self.file_path)
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data