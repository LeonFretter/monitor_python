import json
import os

class Config:
    def __init__(self):
        folder_path = os.path.abspath( os.path.dirname(__file__) )
        config_path = folder_path + '/config.json'
        self.config_file = open( config_path, 'r+' )
    
    def read(self):
        config = json.load(self.config_file)
        return config

    def write(self, content: dict) -> None:
        json.dump(content, self.config_file, indent=4)