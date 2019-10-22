import os
from pathlib import Path

import utils.wait
import json
import jsonpickle
import utils.discover as discover


class PackageJsonObj:
    def init_with_values(self, package_name: str, display_name: str, unity_min_version: str, description: str,
                         version: str, dependencies: dict):
        self.name = package_name
        self.displayName = display_name

        if unity_min_version != "":
            self.unity = unity_min_version

        self.description = description
        self.version = version
        self.dependencies = dependencies

    def init_from_dict(self, init_dict: dict):
        for key in init_dict:
            setattr(self, key, init_dict[key])

    def get(self, name):
        return getattr(self, name, '')

    def set(self, name, value):
        setattr(self, name, value)

    def getDependencies(self):
        return self.get('dependencies')

    def setDependencies(self, deps: dict):
        self.set('dependencies', deps)


class PackageManager:
    def __init__(self, package_root_path: Path):
        package_root_path = Path(package_root_path)
        if not package_root_path.exists():
            print("Warning: Package root does not exist.")

        self.package_root_path = package_root_path
        self.package_json_path = package_root_path.joinpath("package.json")

    def exists(self):
        return discover.package_json_exist_in_directory(self.package_root_path)

    def get_dependencies(self):
        print("Dependencies (one per line, blank to terminate):")
        inputs = {}

        while True:
            last_input = input("> ")
            if last_input == "":
                break
            else:
                parsed = last_input.split(":")
                inputs[parsed[0]] = parsed[1]

        return inputs

    def create(self):
        package_name = input("Package name: ")
        display_name = input("Display name: ")
        unity_min_version = input("Unity min version (blank if doesn't apply): ")
        description = input("Description: ")
        version = input("Version: ")
        dependencies = self.get_dependencies()

        if not self.package_root_path.exists():
            os.makedirs(str(self.package_root_path))

        jsonObj = PackageJsonObj()
        jsonObj.init_with_values(package_name, display_name, unity_min_version, description, version, dependencies)
        self.save(jsonObj)

    def refresh(self):
        self.read()

    def read(self):
        with open(self.package_json_path, "r") as fp:
            json = None
            try:
                json = jsonpickle.decode(fp.read())
            except Exception as ex:
                raise Exception("package.json file is not valid JSON (" + str(ex) + ")")
            jsonObj = PackageJsonObj()
            jsonObj.init_from_dict(json)
            return jsonObj

    def save(self, jsonObj: PackageJsonObj):
        with open(self.package_json_path, "w+") as fp:
            fp.write(json.dumps(json.loads(jsonpickle.encode(jsonObj, unpicklable=False)), indent=4, sort_keys=True))
