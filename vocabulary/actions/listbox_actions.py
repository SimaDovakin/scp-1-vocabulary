import tkinter as tk


def onselect(event, text_box):
    word_list = event.widget

    if word_list.curselection():
        selection_index = int(word_list.curselection()[0])
        word = word_list.get(selection_index)

        word_data = next(
            filter(
                lambda item: item['word'] == word,
                word_list.word_list
            )
        )

        text_box.word_data = word_data
        text_box.setup_state()
