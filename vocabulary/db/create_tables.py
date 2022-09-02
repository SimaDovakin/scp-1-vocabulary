from vocabulary.db.decorators import db_query


@db_query
def create_word_table(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY,
            word TEXT UNIQUE NOT NULL,
            translation TEXT
        );
    """
    result = cursor.execute(query)

    return result


def create_tables() -> None:
    """
        Creates all tables of the app.
    """
    create_word_table()
