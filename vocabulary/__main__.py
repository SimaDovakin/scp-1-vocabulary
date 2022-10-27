import tkinter as tk

from vocabulary.config.initialize import set_words_to_state
from vocabulary.db.create_tables import create_tables
from vocabulary.db.selects import get_words
from vocabulary.ui import MainFrame


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Vocabulary')
    root.geometry('1000x600')

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    create_tables()

    mock_state = {
        'words': []
    }
    set_words_to_state(
        mock_state,
        get_words()
    )

    main_frame = MainFrame(root, bg='#505050')

    main_frame.setup_layout()
    main_frame.setup_state(state=mock_state)
    main_frame.setup_actions()

    main_frame.grid(row=0, column=0, sticky='WNES')

    root.mainloop()
