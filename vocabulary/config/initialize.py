from functools import lru_cache
import os
from pathlib import Path


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
