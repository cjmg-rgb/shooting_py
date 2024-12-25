import json

class Config:
    def __init__(self, file_path):
        with open(file_path, "r") as file:
            self.config = json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)