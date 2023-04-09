import tkinter as tk

from vocabulary.db.updates import update_word_description


def oninput(event, list_box):
    text_box = event.widget

    selected_word_indexes = list_box.curselection()
    if not selected_word_indexes:
        return

    word = list_box.get(selected_word_indexes[0])
    description = text_box.get("1.0", tk.END)
    description = description or ""

    update_word_description(word, description)
