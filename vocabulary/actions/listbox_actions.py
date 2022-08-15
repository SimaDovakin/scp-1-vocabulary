def onselect(event, main_state):
    word_list = event.widget
    selection_index = int(word_list.curselection()[0])
    word = word_list.get(selection_index)
    print(f"You selected word {word!r}: index {selection_index!r}")
