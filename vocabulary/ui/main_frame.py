import tkinter as tk

from .sidebar import SideBar


class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sidebar = SideBar(
            self,
            bg='#ffffff'
        )
        self.main_widget = tk.Text(self)

    def setup_layout(self):
        print(f"Setup layout of {self.__class__.__name__}.")

        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=0, minsize=200)
        self.rowconfigure(0, weight=1)

        self.sidebar.setup_layout()
        self.sidebar.grid(row=0, column=0, sticky='WNES')
        self.main_widget.grid(row=0, column=1, sticky='WNES')
