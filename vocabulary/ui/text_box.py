import tkinter as tk
from typing import Optional

from vocabulary.actions.textbox_actions import oninput


class TextBox(tk.Text):
    """
        Text box where you can add some notes (or translations) of
    the word.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_state(self, word_data: Optional[dict] = None) -> None:
        word_data = word_data if word_data is not None else {}

        if word_data:
            translation = word_data.get('translation', 'Translation not found.')
        else:
            translation = ''

        self.delete('1.0', tk.END)
        self.insert(tk.END, translation)

    def setup_actions(self):
        word_list = self.master.sidebar.word_list_widget

        self.bind('<KeyRelease>', lambda e: oninput(e, word_list))
