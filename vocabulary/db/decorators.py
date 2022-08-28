from contextlib import closing
import sqlite3

from vocabulary.config.initialize import init_config_dir
from vocabulary.config import config


def db_query(func):
    def wrapper(*args, **kwargs):
        with closing(
            sqlite3.connect(init_config_dir() / config.DB_NAME)
        ) as connection:
            with closing(connection.cursor()) as cursor:
                result = func(cursor, *args, **kwargs)

        return result
    return wrapper
