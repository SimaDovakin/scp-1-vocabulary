import tkinter as tk
from typing import Optional

from vocabulary.actions.listbox_actions import onselect


class WordList(tk.Listbox):

    def __init__(self, *args, word_list: Optional[list] = None, **kwargs):
        print('Word List', args, kwargs)
        super().__init__(*args, **kwargs)
        self.word_list = [] if word_list is None else word_list

    def setup_state(self) -> None:
        for word_data in self.word_list:
            self.insert(tk.END, word_data['word'])

    def setup_actions(self):
        self.bind('<<ListboxSelect>>', lambda e: onselect(e, self.word_list))
