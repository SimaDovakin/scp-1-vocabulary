import tkinter as tk


class SideBar(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_input = tk.Entry(self)
        self.word_list = tk.Listbox(self)

    def setup_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.word_input.grid(row=0, column=0, sticky='WE')
        self.word_list.grid(row=1, column=0, sticky='WNES')
