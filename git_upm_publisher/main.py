import os
from git_upm_publisher.utils.config_reader import Config
from git_upm_publisher.utils.package_manager import PackageManager
from git_upm_publisher import config_maker
from git_upm_publisher import package_json_creator
from git_upm_publisher import package_json_updater
from git_upm_publisher import upm_publisher


def run_config_maker():
    if os.path.exists("config.json"):
        overwrite_config = input("You already have a config.json file. Do you want to reconfigure it? (y/n): ")
        if overwrite_config != 'y':
            return
    print("Starting config_maker")
    config_maker.main()


def run_package_makers(package: PackageManager):
    if package.exists():
        package.read()
        print("You already have a package.json file. You can...")
        print("0. Use it as is")
        print("1. Recreate it completely")
        print("2. Update it partially")
        opt = int(input("Enter the index of your choice: "))
        if opt == 0:
            return
        if opt == 1:
            print("Starting package_json_creator")
            package_json_creator.main()
        if opt == 2:
            print("Starting package_json_updater")
            package_json_updater.main()
    else:
        print("Starting package_json_creator")
        package_json_creator.main()


def run_upm_publisher():
    print("Starting upm_publisher")
    upm_publisher.main()


def main():
    config = Config()

    run_config_maker()
    config.refresh()
    package = PackageManager(config.package_root_path())

    run_package_makers(package)
    package.refresh()

    run_upm_publisher()


if __name__ == '__main__':
    main()
    input("Press any key to exit.")
