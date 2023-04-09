import tkinter as tk

from vocabulary.db.deletes import delete_word
from vocabulary.db.selects import get_word_description


def onselect(event, text_box):
    list_box = event.widget

    selected_word_indexes = list_box.curselection()
    if not selected_word_indexes:
        return

    word = list_box.get(selected_word_indexes[0])
    word_description = get_word_description(word)
    word_description = word_description or ""

    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, word_description)


def onpressdelete(event):
    list_box = event.widget

    selected_word_indexes = list_box.curselection()
    if not selected_word_indexes:
        return

    selected_word = list_box.get(selected_word_indexes[0])

    delete_word(selected_word)

    list_box.delete(selected_word_indexes[0])
