from typing import List

import PySimpleGUI as ui

from gui.custom_event_handler import CustomEventHandler
from gui.event_params import EventParams
from gui.layout_addendum import LayoutAddendum
from utils.utility import list_to_dict


class DynamicJsonEditorWindow:
    def __init__(self, json: dict = {}, layout_addendum: LayoutAddendum = LayoutAddendum(), window_title: str = "",
                 custom_event_handlers: List[CustomEventHandler] = []):
        self.custom_event_handlers = custom_event_handlers
        self.window_title = window_title
        self.layout_addendum = layout_addendum
        self.json = json

    def launch(self, values: dict = None) -> dict:
        if values is None:
            values = self.json

        layout = []
        layout = self.layout_addendum.append_header_to(layout)

        layout += [[ui.InputText(name, size=(15, 1)), ui.InputText(value, size=(15, 1)), ui.Button('-', key='del:' + name)]
                   for name, value in values.items()]
        layout = self.layout_addendum.append_after_list_to(layout)

        layout.append([ui.Button(button_text='+')])
        layout = self.layout_addendum.append_after_plus_button_to(layout)

        layout.append([ui.Submit(button_text='Save'), ui.Cancel()])
        layout = self.layout_addendum.append_footer_to(layout)

        window = ui.Window(self.window_title, layout, auto_size_buttons=True)

        while True:
            handled = False
            event, values = window.Read()
            values = list_to_dict(values)

            window.disable()

            if event.startswith('del:'):
                key_to_delete = event.split(':')[1]
                del values[key_to_delete]
                window.close()
                return self.launch(values)

            if event is '+':
                handled = True
                values[''] = ''
                window.close()
                return self.launch(values)

            elif (event is 'Cancel') | (event is None):
                handled = True
                window.close()
                return self.json

            elif event is 'Save':
                handled = True
                window.close()
                return values

            elif self.custom_event_handlers is not None:
                for eh in self.custom_event_handlers:
                    response = eh.handle(EventParams(event, values))

                    if response.handled:
                        handled = True
                        if response.should_close:
                            window.close()
                            return self.launch(response.values)

            if not handled:
                raise Exception("event is not handled: " + event)

            window.enable()
            window.bring_to_front()
            window.TKroot.focus_force()


if __name__ is '__main__':
    la = LayoutAddendum(header=             [[ui.Text("header")]],
                        after_list=         [[ui.Text("after list")]],
                        after_plus_button=  [[ui.Text("after plus button")]],
                        footer=             [[ui.Text("footer")]]
                        )

    dje = DynamicJsonEditorWindow({'a': 'b'}, window_title="title", layout_addendum=la)
    returned = dje.launch()
    print("returned: " + str(returned))
