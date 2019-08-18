import json
import os

class Config:
    def __init__(self):
        with open("config.json", "r") as config_file:
            self.config = json.load(config_file)

    def package_root_path(self):
        return self.config["package_root_path"]

    def repo_root_path(self):
        return self.config["repo_root_path"]
        