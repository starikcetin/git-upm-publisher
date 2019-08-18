try:
    from utils.package_manager import PackageManager
    from utils.config_reader import Config
    import jsonpickle
    import os

    config = Config()
    pm = PackageManager(config.package_root_path())

    if not pm.exists():
        raise Exception("Cannot locate package.json")

    jsonObj = pm.read()
    
    print("Enter the key of the property to change, one per line. 'c' to cancel. 's' to save.")

    while True:
        property_to_change = input("> ")

        if(property_to_change == "c"):
            raise Exception("Cancelled by user")
        elif(property_to_change == "s"):
            break

        current_value = jsonObj.get(property_to_change)
        print("Current value: " + str(current_value))
        new_value = input("New value: ")
        jsonObj.set(property_to_change, new_value)

    pm.save(jsonObj)
    

except Exception as exc:
    print("Error: " + str(exc))

input("Press any key to exit.")
