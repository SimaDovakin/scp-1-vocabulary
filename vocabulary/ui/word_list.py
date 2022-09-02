import tkinter as tk
from typing import Optional

from vocabulary.actions.listbox_actions import onselect


class WordList(tk.Listbox):
    """
        Contains the word list of vocabulary.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_state(self, word_list: Optional[list] = None) -> None:
        word_list = word_list if word_list is not None else []

        if word_list:
            for word_data in word_list:
                self.insert(tk.END, word_data['word'])

    def setup_actions(self):
        text_box = self.master.master.text_box
        self.bind('<<ListboxSelect>>', lambda e: onselect(e, text_box))
