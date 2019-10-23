from pathlib import Path

from utils.prompt import Prompt


class ConfigFileFinder(Prompt):
    def find_config_file(self) -> Path:
        return super().file()
