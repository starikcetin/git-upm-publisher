import os
import json
import jsonpickle
from git_upm_publisher.utils import discover
from git_upm_publisher.utils.package_json_obj import PackageJsonObj


class PackageManager:
    def __init__(self, package_root_path: str):
        if not os.path.exists(package_root_path):
            print("Warning: Package root does not exist.")

        self.package_root_path = package_root_path
        self.package_json_path = os.path.join(package_root_path, "package.json")

    def exists(self):
        return discover.package_json_exist_in_directory(self.package_root_path)

    @staticmethod
    def get_dependencies():
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

        if not os.path.exists(self.package_root_path):
            os.makedirs(self.package_root_path)

        json_obj = PackageJsonObj()
        json_obj.init_with_values(package_name, display_name, unity_min_version, description, version, dependencies)
        self.save(json_obj)

    def refresh(self):
        self.read()

    def read(self):
        with open(self.package_json_path, "r") as fp:
            try:
                json_decoded = jsonpickle.decode(fp.read())
            except Exception as ex:
                raise Exception("package.json file is not valid JSON (" + str(ex) + ")")
            json_obj = PackageJsonObj()
            json_obj.init_from_dict(json_decoded)
            return json_obj

    def save(self, json_obj: PackageJsonObj):
        with open(self.package_json_path, "w+") as fp:
            fp.write(json.dumps(json.loads(jsonpickle.encode(json_obj, unpicklable=False)), indent=4, sort_keys=True))
