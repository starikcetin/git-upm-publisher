from pathlib import Path
import PySimpleGUI as ui
from PythonJsonEditorWindow import JsonEditorWindow, EventParams, EventResponse, CustomEventHandler, LayoutAddendum

from utils.config_reader import Config
from utils.package_manager import PackageManager


class PackageJsonEditorWindow:
    def __init__(self, package_manager: PackageManager):
        self.package_manager = package_manager
        self.json = package_manager.read()

    def _dependency_edit_window(self, json: dict = None):
        if json is None:
            json = self.json.get_dependencies()

        editor = JsonEditorWindow(json, window_title="Dependency Editor")

        new_deps = editor.launch()
        return new_deps

    def _main_window_edit_event_handler(self, params: EventParams) -> EventResponse:
        dependencies_result = self._dependency_edit_window()
        self.json.set_dependencies(dependencies_result)
        return EventResponse(True, False, params.values)

    def launch(self, json: dict = None):
        if json is None:
            json = self.json.__dict__

        # split out dependencies
        json_without_dependencies = {k: v for k, v in json.items() if k != 'dependencies'}

        # edit json without dependencies
        ceh = [CustomEventHandler("Edit...", self._main_window_edit_event_handler)]
        la = LayoutAddendum(after_list=[
            [ui.Text('Dependencies', size=(15, 1)), ui.Button(button_text='Edit...', auto_size_button=True)]])
        editor = JsonEditorWindow(json_without_dependencies, window_title="package.json editor", layout_addendum=la,
                                  custom_event_handlers=ceh)

        result = editor.launch()

        # merge dependencies back in
        json_dependencies = self.json.get_dependencies()
        result.update(json_dependencies)

        return result


if __name__ == "__main__":
    c = Config(Path("../config.json"))
    pm = PackageManager(c.package_root_path())
    pje = PackageJsonEditorWindow(pm)
    response = pje.launch()
    print(response)
