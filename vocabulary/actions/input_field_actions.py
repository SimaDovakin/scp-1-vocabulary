import tkinter as tk

from vocabulary.db.creates import create_word


def onclick_enter(event, input_field, listbox):
    word = input_field.get().strip()

    if word:
        create_word(word)

        listbox.insert(tk.END, word)
        input_field.delete(0, tk.END)
