import json
import os

class Config:
    def __init__(self):
        folder_path = os.path.abspath( os.path.dirname(__file__) )
        config_path = folder_path + '/config.json'
        if not os.path.isfile(config_path):
            os.mknod(config_path)
        self.config_file = open( config_path, 'r+' )
    
    def read(self) -> dict:
        self.config_file.seek(0)
        return json.load(self.config_file)

    def write(self, content: dict) -> None:
        self.config_file.seek(0)
        json.dump(content, self.config_file, indent=4)