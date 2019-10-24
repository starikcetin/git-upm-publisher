from pathlib import Path


class ConfigWrapper:
    def __init__(self, config_file_path: Path):
        self.config_file_path = config_file_path

        self.repo_root_folder_path: Path = None
        self.package_root_folder_path: Path = None
        self.package_file_path: Path = self.package_root_folder_path.joinpath("package.json")

