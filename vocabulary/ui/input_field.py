import tkinter as tk

from vocabulary.actions.input_field_actions import onclick_enter


class InputField(tk.Entry):
    """
        Input field for entering new words and saving them.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_actions(self):
        listbox = self.master.word_list_widget

        self.bind(
            '<Return>',
            lambda event: onclick_enter(event, self, listbox)
        )
