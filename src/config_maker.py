try:
    import utils.discover as discover
    from utils.config_reader import Config
    from tkinter import filedialog
    from tkinter import *
    import os

    tkroot = Tk()
    tkroot.withdraw()

    if len(list(discover.pattern('config.json', '.'))) is not 0:
        print("WARNING: You already have a config.json file. This procedure will overwrite it.")

    c = Config()

    def writeConfig(repo_root_path, package_root_path):
        repo_root_path = str(repo_root_path)
        package_root_path = str(package_root_path)
        print("Writing config.")
        print("Repo root path: " + repo_root_path)
        print("Package root path: " + package_root_path)
        c.package_root_path(package_root_path)
        c.repo_root_path(repo_root_path)
        c.save()

    def pickPackageJson(package_jsons):
        print("Pick package.json")
        i = 0

        for package_json in package_jsons:
            print(str(i) + '.\t' + package_json)
            i += 1
        
        opt = input("Enter the index of the file you wish to use, or leave empty to select manually via a dialog: ")
        
        if opt is '':
            return -1

        return package_jsons[int(opt)]

    #repo_root_path = input("Repo root path (can be relative): ")
    repo_root_path = filedialog.askdirectory(title="Select the root directory of the Git Repository...", initialdir='.', mustexist=True)
    package_root_path = None

    perform_search = input("Search for 'package.json' files to automatically obtain the package root path? (y/n): ")
    
    if perform_search is 'y':
        print("Searching for package.json files...")
        package_jsons = list(map(lambda p : str(discover.make_relative(p, '.')), discover.package_json_recursive(repo_root_path)))
        count = len(package_jsons)

        if count is 0:
            print("Cannot find any package.json file in the repository.")
            print("You need to manually enter your package root path.")
            #package_root_path = input("Package root path (can be relative): ")
            package_root_path = filedialog.askdirectory(title="Select the root directory of UPM package...", initialdir=repo_root_path, mustexist=True)
        elif count is 1:
            print("Found a single package.json file.")
            package_root_path = discover.directory_of_file(package_jsons[0])
        else:
            print("There are multiple package.json files in the repository.")
            package_json_path = pickPackageJson(package_jsons)

            if package_json_path is -1:
                package_root_path = filedialog.askdirectory(title="Select the root directory of UPM package...", initialdir=repo_root_path, mustexist=True)
            else:
                package_root_path = discover.directory_of_file(package_json_path)
    else:
        #package_root_path = input("Package root path (can be relative): ")
        package_root_path = filedialog.askdirectory(title="Select the root directory of UPM package...", initialdir=repo_root_path, mustexist=True)

    repo_root_path = discover.make_relative(repo_root_path, '.')
    package_root_path = discover.make_relative(package_root_path, '.')
    writeConfig(repo_root_path, package_root_path)

except Exception as ex:
    print("Error: " + str(ex))

input("Press any key to exit.")