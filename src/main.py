try:
    import os
    from utils.config_reader import Config
    import utils.discover as discover
    from pathlib import Path

    config_file_path = Path(input("Enter config file path: ")).joinpath("config.json")
    config = Config(config_file_path)

    def cm():
        if os.path.exists("config.json"):
            overwrite_config = input("You already have a config.json file. Do you want to reconfigure it? (y/n): ")
            if overwrite_config is not 'y':
                return
        print("Starting config_maker")
        import config_maker

    cm()
    config.refresh()
    from utils.package_manager import PackageManager
    package = PackageManager(config.package_root_path())

    def pj():
        if package.exists():
            package.read()
            print("You already have a package.json file. You can...")
            print("0. Use it as is")
            print("1. Recreate it completely")
            print("2. Update it partially")
            opt = int(input("Enter the index of your choice: "))
            if opt is 0:
                return
            if opt is 1:
                print("Starting package_json_creator")
                import package_json_creator
            if opt is 2:
                print("Starting package_json_updater")
                import package_json_updater
        else:
            print("Starting package_json_creator")
            import package_json_creator

    pj()
    package.refresh()

    def up():
        print("Starting upm_publisher")
        import upm_publisher

    up()

except Exception as ex:
    print("Error: " + str(ex))

input("Press any key to exit.")