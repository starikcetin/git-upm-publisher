from utils.config_file_finder import ConfigFileFinder
from modules.publisher import Publisher
from utils.git import Git
from wrappers.config_wrapper import ConfigWrapper
from wrappers.package_wrapper import PackageWrapper


class GitUpmPublisher:
    def __init__(self):
        config_file_path = ConfigFileFinder.find()

        self.config_wrapper: ConfigWrapper = ConfigWrapper(config_file_path)
        self.package_wrapper: PackageWrapper = PackageWrapper(self.config_wrapper.package_file_path)
        self.git: Git = Git(self.config_wrapper.repo_root_folder_path)
        self.publisher: Publisher = Publisher(self.config_wrapper, self.package_wrapper, self.git)

    def run(self):
        self.publisher.publish()


if __name__ == '__main__':
    GitUpmPublisher().run()
