import os
import utils.wait
import json
import jsonpickle

class PackageJsonObj:
    def __init__(self, package_name: str, display_name: str, unity_min_version: str, description: str, version: str, dependencies: dict):
        self.Name = package_name
        self.DisplayName = display_name

        if unity_min_version != "":
            self.Unity = unity_min_version

        self.Description = description
        self.Version = version
        self.Dependencies = dependencies


class PackageManager:
    def __init__(self, package_root_path: str):
        if not os.path.exists(package_root_path):
             print("Package root does not exist.")

        self.package_root_path = package_root_path
        self.package_json_path = os.path.join(package_root_path, "package.json")

    def package_json_exists(self):
        return os.path.exists(self.package_json_path)

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

    def create_package_json(self):
        package_name = input("Package name: ")
        display_name = input("Display name: ")
        unity_min_version = input("Unity min version (blank if doesn't apply): ")
        description = input("Description: ")
        version = input("Version: ")
        dependencies = self.get_dependencies()

        if not os.path.exists(self.package_root_path):
            os.makedirs(self.package_root_path)

        with open(self.package_json_path, "w+") as fp:
            jsonObj = PackageJsonObj(package_name, display_name, unity_min_version, description, version, dependencies)
            fp.write(json.dumps(json.loads(jsonpickle.encode(jsonObj, unpicklable=False)), indent=4, sort_keys=True))
