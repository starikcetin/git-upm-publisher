from utils.config_reader import Config
from utils.package_manager import PackageManager

config = Config()

pm = PackageManager(config.package_root_path())
packageJsonExists = pm.package_json_exists()

if packageJsonExists:
    print("WARNING: You already have a package.json, this procedure will overwrite it!")

pm.create_package_json()

print("Done. File location: " + pm.package_json_path)
print("Don't forget to generate the meta file for the package.json by switching to Unity Editor.")
input("Press any key to exit.")
