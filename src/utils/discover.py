from pathlib import Path

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
        path = Path(path)
    if anchor is not Path:
        anchor = Path(anchor)

    if anchor in path.parents:
        return path.relative_to(anchor)
    else:
        print("Error while making the path relative: Anchor is not a parent directory of path. Returning absolute.")
        return path.absolute()
