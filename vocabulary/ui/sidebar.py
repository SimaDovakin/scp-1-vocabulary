import tkinter as tk
from typing import Optional

from .word_list import WordList


class SideBar(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_input = tk.Entry(self)
        self.word_list_widget = WordList(self)

    def setup_layout(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.word_input.grid(row=0, column=0, sticky='WE')
        self.word_list_widget.grid(row=1, column=0, sticky='WNES')

    def setup_state(self, word_list: Optional[list] = None) -> None:
        word_list = word_list if word_list is not None else []
        if word_list:
            self.word_list_widget.setup_state(word_list)

    def setup_actions(self):
        self.word_list_widget.setup_actions()
