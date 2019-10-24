import os
import subprocess
from pathlib import Path


class CLI:
    @staticmethod
    def cwd(path: Path = None) -> Path:
        if path is not None:
            os.chdir(path)
        return Path.cwd()

    @staticmethod
    def run(command: str, args: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run([command] + args, shell=True)
