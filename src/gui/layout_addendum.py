import copy
from typing import List
import PySimpleGUI as ui


class LayoutAddendum:
    def __init__(self,
                 header: List[List[ui.Element]] = None,
                 after_list: List[List[ui.Element]] = None,
                 after_plus_button: List[List[ui.Element]] = None,
                 footer: List[List[ui.Element]] = None
                 ):
        self.header = lambda: copy.deepcopy(header)
        self.after_list = lambda: copy.deepcopy(after_list)
        self.after_plus_button = lambda: copy.deepcopy(after_plus_button)
        self.footer = lambda: copy.deepcopy(footer)

    def append_header_to(self, layout: List[List[ui.Element]]) -> List[List[ui.Element]]:
        if self.header() is None:
            return layout
        return layout + self.header()

    def append_after_list_to(self, layout: List[List[ui.Element]]) -> List[List[ui.Element]]:
        if self.after_list() is None:
            return layout
        return layout + self.after_list()

    def append_after_plus_button_to(self, layout: List[List[ui.Element]]) -> List[List[ui.Element]]:
        if self.after_plus_button() is None:
            return layout
        return layout + self.after_plus_button()

    def append_footer_to(self, layout: List[List[ui.Element]]) -> List[List[ui.Element]]:
        if self.footer() is None:
            return layout
        return layout + self.footer()
