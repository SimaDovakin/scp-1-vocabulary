import os
from pathlib import Path


def init_config_dir() -> Path:
    config_path = Path.home() / '.pyvocabulary'
    if not os.path.exists(config_path):
        os.mkdir(config_path)

    return config_path
