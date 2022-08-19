import tkinter as tk


def onselect(event, text_box):
    word_list = event.widget

    if word_list.curselection():
        selection_index = int(word_list.curselection()[0])
        word = word_list.get(selection_index)

        translation = next(
            filter(
                lambda item: item['word'] == word,
                word_list.word_list
            )
        ).get('translation')

        text_box.delete('1.0', tk.END)

        if translation:
            text_box.insert(tk.END, translation)
        else:
            text_box.insert(tk.END, 'Content not found.')
