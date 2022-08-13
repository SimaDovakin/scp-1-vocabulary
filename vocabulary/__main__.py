import tkinter as tk

from .ui import MainFrame


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Vocabulary')
    root.geometry('1000x600')

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_frame = MainFrame(root, bg='#505050')
    main_frame.grid(row=0, column=0, sticky='WNES')

    root.mainloop()
