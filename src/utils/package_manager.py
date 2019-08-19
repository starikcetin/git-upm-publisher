import os
import utils.wait
import json
import jsonpickle

class PackageJsonObj:
    def initWithValues(self, package_name: str, display_name: str, unity_min_version: str, description: str, version: str, dependencies: dict):
        self.name = package_name
        self.displayName = display_name

        if unity_min_version != "":
            self.unity = unity_min_version

        self.description = description
        self.version = version
        self.dependencies = dependencies

    def initFromDict(self, init_dict: dict):
        for key in init_dict:
            setattr(self, key, init_dict[key])

    def get(self, name):
        return getattr(self, name)

    def set(self, name, value):
        setattr(self, name, value)


class PackageManager:
    def __init__(self, package_root_path: str):
        if not os.path.exists(package_root_path):
             print("Warning: Package root does not exist.")

        self.package_root_path = package_root_path
        self.package_json_path = os.path.join(package_root_path, "package.json")

    def exists(self):
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

    def create(self):
        package_name = input("Package name: ")
        display_name = input("Display name: ")
        unity_min_version = input("Unity min version (blank if doesn't apply): ")
        description = input("Description: ")
        version = input("Version: ")
        dependencies = self.get_dependencies()

        if not os.path.exists(self.package_root_path):
            os.makedirs(self.package_root_path)

        jsonObj = PackageJsonObj()
        jsonObj.initWithValues(package_name, display_name, unity_min_version, description, version, dependencies)
        self.save(jsonObj)

    def read(self):
        with open(self.package_json_path, "r") as fp:
            json = None
            try:
                json = jsonpickle.decode(fp.read())
            except Exception as ex:
                raise Exception("package.json file is not valid JSON (" + str(ex) + ")")
            jsonObj = PackageJsonObj()
            jsonObj.initFromDict(json)
            return jsonObj

    def save(self, jsonObj:PackageJsonObj):
        with open(self.package_json_path, "w+") as fp:
            fp.write(json.dumps(json.loads(jsonpickle.encode(jsonObj, unpicklable=False)), indent=4, sort_keys=True))
