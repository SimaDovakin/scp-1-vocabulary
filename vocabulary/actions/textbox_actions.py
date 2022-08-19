import tkinter as tk


def oninput(event):
    word_data = event.widget.word_data
    current_word = event.widget.get('1.0', tk.END)
    if word_data['translation'] != current_word.strip():
        word_data['translation'] = current_word.strip()
