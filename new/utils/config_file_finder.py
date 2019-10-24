from pathlib import Path

from utils.prompt import Prompt


class ConfigFileFinder:
    @staticmethod
    def find() -> Path:
        return Prompt.file()
        pass
