from git_upm_publisher.utils.config_reader import Config
from git_upm_publisher.utils.git_manager import Git
from git_upm_publisher.utils.package_manager import PackageManager


def main():
    config = Config()
    git = Git(config.repo_root_path())
    pm = PackageManager(config.package_root_path())

    package = pm.read()
    package_version = package.get("version")
    print("Version from package.json: " + package_version)
    version_tag = package_version  # + "-upm"
    print("Version tag: " + version_tag)

    print(git.status())
    should_push = input("Fetch before starting? (y/n): ")

    if should_push == 'y':
        git.fetch()
        print(git.status())

    if git.is_dirty():
        print("You have outstanding changes in your repository.")
        print("You have a couple of options:")
        print("\t0. Cancel and deal with them manually (RECOMMENDED)")
        print("\t1. Commit -> publish -> soft reset (will try to preserve changes)")
        print("\t2. Clean -> publish (will erase all changes)")
        opt = input("Pick an index: ")

        if opt == '0':
            raise Exception("Cancelled by user.")
        elif opt == '1':
            temp_commit_message = "!!! TEMP COMMIT CREATED BY git-upm-publisher, WILL BE SOFT RESET !!!\n\nThis commit should be gone after everything is done, if you see it in your repository after publisher is done, something went wrong. Send me a bug report over GitHub.\n\nYou can manually soft-reset this commit if you wish."
            git.commit_all(temp_commit_message)
            git.publish(config.package_root_path(), "upm release", "upm", version_tag)
            git.soft_reset_last_commit()
        elif opt == '2':
            git.clean()
            git.publish(config.package_root_path(), "upm release", "upm", version_tag)
        else:
            raise Exception("Wrong option index.")
    else:
        git.publish(config.package_root_path(), "upm release", "upm", version_tag)

    print(git.status())
    should_push = input("Push everything? (y/n): ")

    if should_push == 'y':
        git.push_all()
        print(git.status())


if __name__ == '__main__':
    main()
    input("Press any key to exit.")
