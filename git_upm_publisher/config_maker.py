from git_upm_publisher.utils.config_reader import Config
from git_upm_publisher.utils import discover


def main():
    if len(list(discover.pattern('config.json', '.'))) != 0:
        print("WARNING: You already have a config.json file. This procedure will overwrite it.")
        c = Config()

        repo_root_path = discover.ask_repo_root()

        perform_search = input(
            "Search for 'package.json' files to automatically obtain the package root path? (y/n): ")

        if perform_search == 'y':
            print("Searching for package.json files...")
            package_jsons = list(
                map(lambda p: str(discover.make_relative(p, '.')),
                    discover.package_json_recursive(repo_root_path)))
            count = len(package_jsons)

            if count == 0:
                print("Cannot find any package.json file in the repository.")
                print("You need to manually enter your package root path.")
                package_root_path = discover.ask_package_root(repo_root_path)
            elif count == 1:
                print("Found a single package.json file.")
                package_root_path = discover.directory_of_file(package_jsons[0])
            else:
                print("There are multiple package.json files in the repository.")
                package_json_path = pick_package_json(package_jsons)

                if package_json_path == -1:
                    package_root_path = discover.ask_package_root(repo_root_path)
                else:
                    package_root_path = discover.directory_of_file(package_json_path)
        else:
            package_root_path = discover.ask_package_root(repo_root_path)

        repo_root_path = discover.make_relative(repo_root_path, '.')
        package_root_path = discover.make_relative(package_root_path, '.')
        write_config(repo_root_path, package_root_path, c)


def write_config(repo_root_path, package_root_path, c: Config):
    repo_root_path = str(repo_root_path)
    package_root_path = str(package_root_path)
    print("Writing config.")
    print("Repo root path: " + repo_root_path)
    print("Package root path: " + package_root_path)
    c.package_root_path(package_root_path)
    c.repo_root_path(repo_root_path)
    c.save()


def pick_package_json(package_jsons):
    print("Pick package.json")
    i = 0

    for package_json in package_jsons:
        print(str(i) + '.\t' + package_json)
        i += 1

    opt = input("Enter the index of the file you wish to use, or leave empty to select manually via a dialog: ")

    if opt == '':
        return -1

    return package_jsons[int(opt)]


if __name__ == '__main__':
    main()
    input("Press any key to exit.")
