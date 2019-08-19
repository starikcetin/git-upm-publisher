import json
import os

class Config:
    def __init__(self):
        self.read()

    def package_root_path(self, value=None):
        if value is not None:
            self.config["package_root_path"] = value
        else:
            return self.config["package_root_path"]

    def repo_root_path(self, value=None):
        if value is not None:
            self.config["repo_root_path"] = value
        else:
            return self.config["repo_root_path"]

    def read(self):
        with open("config.json", "r") as config_file:
            self.config = json.load(config_file)

    def save(self):
        with open("config.json", "w+") as config_file:
            config_file.write(json.dumps(self.config, indent=4, sort_keys=True))
