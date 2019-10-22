from pathlib import Path

from utils.config_reader import Config
from utils.package_manager import PackageManager

config = Config(Path(input("Config file path: ").join("config.json")))

pm = PackageManager(config.package_root_path())
packageJsonExists = pm.exists()

if packageJsonExists:
    print("WARNING: You already have a package.json, this procedure will overwrite it!")

pm.create()

print("Done. File location: " + pm.package_json_path)
print("Don't forget to generate the meta file for the package.json by switching to Unity Editor.")
input("Press any key to exit.")
