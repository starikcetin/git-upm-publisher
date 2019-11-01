from pathlib import Path
import os
from tkinter import filedialog
from tkinter import *

tkroot = Tk()
tkroot.withdraw()

def pattern(pattern_, path):
    for filename in Path(path).glob(pattern_):
        print(filename)
        yield filename

def pattern_recursive(pattern_, path):
    return pattern('**/' + pattern_, path)

def package_json_recursive(path):
    return pattern_recursive('package.json', path)

def directory_of(path):
    p = Path(path)
    if p.is_dir():
        return p
    elif p.is_file():
        return p.parent

def directory_of_file(file):
    p = Path(file)
    assert p.is_file(), 'Path is not a file.'
    return p.parent

def make_relative(path, anchor):
    if path is not Path:
        path = Path(path).absolute()
    if anchor is not Path:
        anchor = Path(anchor).absolute()

    try:
        return Path(os.path.relpath(path, anchor))
    except:
        print("Error while trying to make the path relative. Returning absolute path.")
        return path.absolute()

def ask_directory(title, initialdir, mustexist):
    return filedialog.askdirectory(title=title, initialdir=initialdir, mustexist=mustexist)

def ask_repo_root():
    #repo_root_path = input("Repo root path (can be relative): ")
    return ask_directory("Select the root directory of the Git Repository...", '.', True)

def ask_package_root(initialdir):
    #package_root_path = input("Package root path (can be relative): ")
    return ask_directory("Select the root directory of UPM package...", initialdir, True)

def file_exist_in_directory(directory, filename):
    found = pattern(filename, directory)
    return len(list(found)) > 0

def package_json_exist_in_directory(directory):
    return file_exist_in_directory(directory, "package.json")
