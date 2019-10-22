import PySimpleGUI as ui

from utils.package_manager import PackageManager
from utils.config_reader import Config
from pathlib import Path


def list_to_dict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


class PackageJsonEditor:
    def __init__(self, package_manager: PackageManager):
        self.package_manager = package_manager
        self.json = package_manager.read()

    def dependency_edit_window(self, deps: dict = None):
        if deps is None:
            deps = self.json.getDependencies()

        layout = [
            [ui.Text('Name', size=(30, 1)), ui.Text('URL', size=(60, 1))]
        ]

        for name in deps:
            url = deps[name]
            layout.append([ui.InputText(default_text=name, size=(30, 1)), ui.InputText(default_text=url, size=(60, 1))])

        layout.append([ui.Button(button_text='+')])
        layout.append([ui.Submit(button_text='Save'), ui.Cancel()])

        window = ui.Window('dependency editor', layout)
        event, values = window.Read()

        print(event)
        print(values)

        newDeps = list_to_dict(values)

        if event is '+':
            newDeps[''] = ''
            self.dependency_edit_window(newDeps)

        if event is 'Save':
            newDeps = {k.strip(): v.strip() for k, v in newDeps.items()}
            newDeps = {k: v for k, v in newDeps.items() if (v != '') & (k != '')}
            self.json.setDependencies(newDeps)

        window.close()

    def main_window(self):
        print('main window')
        layout = [
            [ui.Text('Package Name', size=(15, 1)), ui.InputText(default_text=self.json.get("packageName"))],
            [ui.Text('Display Name', size=(15, 1)), ui.InputText(default_text=self.json.get("displayName"))],
            [ui.Text('Description', size=(15, 1)), ui.InputText(default_text=self.json.get("description"))],
            [ui.Text('Author', size=(15, 1)), ui.InputText(default_text=self.json.get("author"))],
            [ui.Text('Licence', size=(15, 1)), ui.InputText(default_text=self.json.get("licence"))],
            [ui.Text('Min. Unity Version', size=(15, 1)), ui.InputText(default_text=self.json.get("unity"))],
            [ui.Text('Dependencies', size=(15, 1)), ui.Button(button_text='Edit...', auto_size_button=True)],
            [ui.Submit(button_text='Save'), ui.Cancel()]
        ]

        window = ui.Window('package.json editor', layout)

        event, values = window.Read()

        while event is 'Edit...':
            self.dependency_edit_window()
            event, values = window.Read()

        print(event)
        print(values)


if __name__ == "__main__":
    c = Config(Path("../config.json"))
    pm = PackageManager(c.package_root_path())
    pje = PackageJsonEditor(pm)
    pje.main_window()
