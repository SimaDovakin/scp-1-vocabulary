import tkinter as tk
from typing import Optional

from .sidebar import SideBar
from .text_box import TextBox


class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sidebar = SideBar(
            self,
            bg='#ffffff'
        )
        self.text_box = TextBox(self)

    def setup_layout(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=0, minsize=200)
        self.rowconfigure(0, weight=1)

        self.sidebar.setup_layout()
        self.sidebar.grid(row=0, column=0, sticky='WNES')
        self.text_box.grid(row=0, column=1, sticky='WNES')

    def setup_state(self, state: Optional[dict] = None) -> None:
        state = state if state is not None else {}
        if state and state['words']:
            self.sidebar.setup_state(state['words'])

        self.text_box.setup_state()

    def setup_actions(self):
        self.sidebar.setup_actions()
        self.text_box.setup_actions()
