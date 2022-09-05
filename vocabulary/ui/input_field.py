import tkinter as tk


class InputField(tk.Entry):
    """
        Input field for entering new words and saving them.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_actions(self):
        pass
