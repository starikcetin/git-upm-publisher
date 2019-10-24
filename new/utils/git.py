from datetime import datetime
from pathlib import Path
from subprocess import CompletedProcess

from git import Repo, TagReference

from utils.cli import CLI


class Git:
    def __init__(self, repo_root_folder_path: Path):
        self.repo_root_folder_path = repo_root_folder_path
        self.repo = Repo(repo_root_folder_path)

    def is_dirty(self) -> bool:
        return self.repo.is_dirty()

    def tag(self, commit: str, name: str, message: str) -> TagReference:
        return self.repo.git.tag("-a", name, commit, "-m", message)

    def commit_all(self, message: str) -> None:
        self.repo.git.add("-A")
        self.repo.git.commit("-m", message)

    def run(self, command: str, args: list[str]) -> CompletedProcess:
        return CLI.run("git", ["-C", self.repo_root_folder_path] + [command] + args)

    def snapshot(self, prefix: Path, message: str, branch_name: str) -> CompletedProcess:
        return self.run("snapshot",
                        ["--prefix", prefix.as_posix(),
                         "--message", message,
                         "--branch", branch_name])

    def soft_reset_last_commit(self) -> str:
        return self.repo.git.reset("--soft", "HEAD~1")

    def clean(self) -> None:
        stash_name = "backup stash before self.repo clean by git-upm-publisher " + str(datetime.now())
        self.repo.git.stash("save", stash_name)
        if self.is_dirty():
            self.repo.git.reset("--hard")

    def push_all(self) -> None:
        self.repo.git.push("--all")
        self.repo.git.push("--tags")

    def status(self) -> str:
        return self.repo.git.status()

    def fetch(self) -> str:
        return self.repo.git.fetch("--all")
