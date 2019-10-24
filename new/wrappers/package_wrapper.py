from pathlib import Path


class PackageWrapper:
    def __init__(self, package_file_path: Path):
        self.package_file_path = package_file_path
        self.version = None

