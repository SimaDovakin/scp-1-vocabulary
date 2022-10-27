from functools import lru_cache
import os
from pathlib import Path
from typing import List, Optional


@lru_cache
def init_config_dir() -> Path:
    """
        Creates a configuration directory of the app if it doesn't
    exists.
    """
    config_path = Path.home() / '.pyvocabulary'
    if not os.path.exists(config_path):
        os.mkdir(config_path)

    return config_path


def set_words_to_state(state, words: Optional[List[tuple]] = None) -> None:
    for word_data in words:
        word = {
            'word': word_data[0],
            'translation': word_data[1]
        }
        state['words'].append(word)
