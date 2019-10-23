from pathlib import Path

from gui.package_json_editor_window import PackageJsonEditorWindow
from utils.config_reader import Config
from utils.package_manager import PackageManager, PackageJsonObj


def edit_with_ui(pm: PackageManager):
    window = PackageJsonEditorWindow(pm)
    result = window.launch()
    json_obj = PackageJsonObj()
    json_obj.init_from_dict(result)
    pm.save(json_obj)


config = Config(Path(input("Config file path: ").join("config.json")))
pm = PackageManager(config.package_root_path())

if not pm.exists():
    raise Exception("Cannot locate package.json")

edit_with_ui(pm)

if __name__ == '__main__':
    input("Press any key to exit.")
