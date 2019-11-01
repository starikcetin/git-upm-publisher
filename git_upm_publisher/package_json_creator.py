from git_upm_publisher.utils.config_reader import Config
from git_upm_publisher.utils.package_manager import PackageManager


def main():
    config = Config()

    pm = PackageManager(config.package_root_path())
    package_json_exists = pm.exists()

    if package_json_exists:
        print("WARNING: You already have a package.json, this procedure will overwrite it!")

    pm.create()

    print("Done. File location: " + pm.package_json_path)
    print("Don't forget to generate the meta file for the package.json by switching to Unity Editor.")


if __name__ == '__main__':
    main()
    input("Press any key to exit.")
