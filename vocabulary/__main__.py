import tkinter as tk

from .ui import MainFrame


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Vocabulary')
    root.geometry('1000x600')

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    mock_state = {
        'words': [
            {
                'word': 'development'
            },
            {
                'word': 'commercial'
            },
            {
                'word': 'news'
            },
            {
                'word': 'happiness'
            }
        ]
    }

    main_frame = MainFrame(root, state=mock_state, bg='#505050')

    main_frame.setup_layout()
    main_frame.setup_state()
    main_frame.setup_actions()

    main_frame.grid(row=0, column=0, sticky='WNES')

    root.mainloop()
