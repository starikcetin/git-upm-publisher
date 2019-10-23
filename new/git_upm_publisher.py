from pathlib import Path

from modules.config_file_finder import ConfigFileFinder
from modules.config_maker import ConfigMaker
from modules.package_maker import PackageMaker
from modules.publisher import Publisher
from wrappers.config_wrapper import ConfigWrapper
from wrappers.package_wrapper import PackageWrapper


class GitUpmPublisher(ConfigFileFinder, ConfigMaker, PackageMaker, Publisher):
    def run(self):
        config_file_path: Path = super().find_config_file()
        config_wrapper: ConfigWrapper = super().make_config(config_file_path)
        package_wrapper: PackageWrapper = super().make_package(config_wrapper)
        super().publish(package_wrapper)


if __name__ == '__main__':
    GitUpmPublisher().run()
