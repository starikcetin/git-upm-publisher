from git import Repo
import os
from datetime import datetime
from subprocess import call

class Git():
    def __init__(self, repo_root_path):
        self.repo_root_path = repo_root_path
        self.dotgit_path = os.path.join(repo_root_path, ".git/")
        assert os.path.exists(self.dotgit_path), "Cannot find the .git folder (are you sure the repo root is correct in the config.json?)"
        self.repo = Repo(repo_root_path)

    def is_dirty(self):
        return self.repo.is_dirty()

    def tag(self, commit, name, message):
        print("Tagging")
        self.repo.git.tag("-a", name, commit, "-m", message)

    def commitAll(self, message):
        print("Comitting all")
        self.repo.git.add("--all")
        self.repo.git.commit("-m", message)

    def publish(self, package_root_path, commit_message, branch_name, version_tag):
        print("Publishing")
        print("branch before publish: " + self.repo.active_branch.name)
        self.repo.git.snapshot("--prefix= " + package_root_path, "--message='" + commit_message + "'", "--branch=" + branch_name)
        print("branch after publish: " + self.repo.active_branch.name)
        self.tag(branch_name, version_tag, version_tag)

    def softResetLastCommit(self):
        print("Soft resetting last commit")
        self.repo.git.reset("--soft", "HEAD~1")

    def clean(self):
        print("Cleaning")
        print("Stashing all")
        self.repo.git.stash("save", "backup stash before repo clean by git-upm-publisher " + str(datetime.now()))

        if self.is_dirty():
            print("Still dirty after stash, doing a hard reset")
            self.repo.git.reset("--hard")

    def pushAll(self):
        print("Pushing")
        self.repo.git.push("--all")
        self.repo.git.push("--tags")

    def status(self):
        print("Status")
        return self.repo.git.status()

    def fetch(self):
        print("Fetching")
        self.repo.git.fetch("--all")
        