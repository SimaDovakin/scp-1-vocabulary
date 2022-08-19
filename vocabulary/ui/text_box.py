import tkinter as tk
from typing import Optional


class TextBox(tk.Text):

    def __init__(self, *args, word_data: Optional[dict] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_data = word_data if word_data else {}

    def setup_state(self) -> None:
        if self.word_data:
            translation = self.word_data.get('translation', 'Translation not found.')
        else:
            translation = ''

        self.delete('1.0', tk.END)
        self.insert(tk.END, translation)

    def setup_actions(self):
        pass
