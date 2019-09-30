import PySimpleGUI as ui
from utils.package_manager import PackageManager
from utils.config_reader import Config


class PackageJsonEditor:
    def __init__(self, package_manager: PackageManager):
        self.package_manager = package_manager
        self.json = package_manager.read()


    def _dependency_edit_window(self):
        print('dependency edit window')
        return -1


    def main_window(self):
        print('main window')
        layout = [
            [ui.Text('Package Name', size=(15,1)),          ui.InputText(default_text=self.json.get("packageName"))],
            [ui.Text('Display Name', size=(15,1)),          ui.InputText(default_text=self.json.get("displayName"))],
            [ui.Text('Description', size=(15,1)),           ui.InputText(default_text=self.json.get("description"))],
            [ui.Text('Author', size=(15,1)),                ui.InputText(default_text=self.json.get("author"))],
            [ui.Text('Licence', size=(15,1)),               ui.InputText(default_text=self.json.get("licence"))],
            [ui.Text('Min. Unity Version', size=(15,1)),    ui.InputText(default_text=self.json.get("unity"))],
            [ui.Text('Dependencies', size=(15,1)),          ui.Button(button_text='Edit...', auto_size_button=True)],
            [ui.Submit(button_text='Save'),                 ui.Cancel()]
        ]

        window = ui.Window('package.json editor', layout)

        event, values = window.Read()

        while event is 'Edit...':
            deps = dependency_edit_window(self)
            event, values = window.Read()

        print(event)
        print(values)


if __name__ == "__main__":
    c = Config()
    c.read()
    pje = PackageJsonEditor(PackageManager(c.package_root_path))
    pje.main_window()
