from git import TagReference

from utils.cli import CLI
from utils.git import Git
from wrappers.config_wrapper import ConfigWrapper
from wrappers.package_wrapper import PackageWrapper


class Publisher:
    def __init__(self, config_wrapper: ConfigWrapper, package_wrapper: PackageWrapper, git: Git):
        self.package_wrapper: PackageWrapper = package_wrapper
        self.config_wrapper: ConfigWrapper = config_wrapper
        self.git: Git = git

    def publish(self) -> TagReference:
        branch_name = "upm"
        tag_name = self.package_wrapper.version
        message = "upm release " + self.package_wrapper.version

        CLI.run("npm", ["install", "-g", "git-snapshot@1.1.2"])
        self.git.snapshot(self.config_wrapper.package_root_folder_path, message, branch_name)
        return self.git.tag(branch_name, tag_name, tag_name)
