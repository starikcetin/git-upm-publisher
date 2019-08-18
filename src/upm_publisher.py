try:
    from utils.config_reader import Config
    from utils.git_manager import Git
    from utils.package_manager import PackageManager
    import os

    config = Config()
    git = Git(config.repo_root_path())
    pm = PackageManager(config.package_root_path())

    package = pm.read()
    package_version = package.get("version")
    print("Version from package.json: "+ package_version)
    version_tag = package_version + "-upm"
    print("Version tag: " + version_tag)

    print(git.status())
    shouldPush = input("Fetch before starting? (y/n): ")
    
    if shouldPush is 'y':
        git.fetch()
        print(git.status())

    if git.is_dirty():
        print("You have outstanding changes in your repository.")
        print("You have a couple of options:")
        print("\t0. Cancel and deal with them manually (RECOMMENDED)")
        print("\t1. Commit -> publish -> soft reset (will try to preserve changes)")
        print("\t2. Clean -> publish (will erase all changes)")
        opt = input("Pick an index: ")

        if opt is '0':
            raise Exception("Cancelled by user.")
        elif opt is '1':
            git.commitAll("!!! TEMP COMMIT CREATED BY git-upm-publisher, WILL BE SOFT RESET !!!")
            git.publish(config.package_root_path(), "upm release", "upm", version_tag)
            git.softResetLastCommit()
        elif opt is '2':
            git.clean()
            git.publish(config.package_root_path(), "upm release", "upm", version_tag)
        else:
            raise Exception("Wrong option index.")
    else:
        git.publish(config.package_root_path(), "upm release", "upm", version_tag)

    print(git.status())
    shouldPush = input("Push everything? (y/n): ")

    if shouldPush is 'y':
        git.pushAll()
        print(git.status())

except Exception as ex:
    print("Error: " + str(ex))

input("Press any key to exit.")
