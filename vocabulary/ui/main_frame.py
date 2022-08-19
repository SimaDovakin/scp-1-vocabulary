import tkinter as tk

from .sidebar import SideBar
from .text_box import TextBox


class MainFrame(tk.Frame):

    def __init__(self, *args, state: dict = {}, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = state
        self.sidebar = SideBar(
            self,
            word_list=self.state['words'],
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

    def setup_state(self):
        if self.state['words']:
            self.sidebar.setup_state()

        self.text_box.setup_state()

    def setup_actions(self):
        self.sidebar.setup_actions()
