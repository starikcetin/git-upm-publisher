from git_upm_publisher.utils.config_reader import Config
from git_upm_publisher.utils.package_manager import PackageManager


def main():
    config = Config()
    pm = PackageManager(config.package_root_path())

    if not pm.exists():
        raise Exception("Cannot locate package.json")

    json_obj = pm.read()

    print("Enter the key of the property to change, one per line. 'c' to cancel. 's' to save.")

    while True:
        property_to_change = input("> ")

        if property_to_change == "c":
            raise Exception("Cancelled by user")
        elif property_to_change == "s":
            break

        try:
            current_value = json_obj.get(property_to_change)
            print("Current value: " + str(current_value))
        except:
            print("Key not found.")
            continue

        new_value = input("New value: ")
        json_obj.set(property_to_change, new_value)

    pm.save(json_obj)
    print("Done.")


if __name__ == '__main__':
    main()
    input("Press any key to exit.")
