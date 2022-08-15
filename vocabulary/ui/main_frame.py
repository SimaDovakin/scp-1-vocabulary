import tkinter as tk

from .sidebar import SideBar


class MainFrame(tk.Frame):

    def __init__(self, *args, state: dict = {}, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = state
        self.sidebar = SideBar(
            self,
            bg='#ffffff'
        )
        self.main_widget = tk.Text(self)

    def setup_layout(self):
        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=0, minsize=200)
        self.rowconfigure(0, weight=1)

        self.sidebar.setup_layout()
        self.sidebar.grid(row=0, column=0, sticky='WNES')
        self.main_widget.grid(row=0, column=1, sticky='WNES')

    def setup_state(self):
        if self.state['words']:
            word_list = self.sidebar.word_list
            for word_data in self.state['words']:
                word_list.insert(tk.END, word_data['word'])
