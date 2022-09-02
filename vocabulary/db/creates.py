from vocabulary.db.decorators import db_query


@db_query
def create_word(cursor, word: str) -> None:
    """
        Inserts a word in the word list table.
    """
    query = """
        INSERT INTO words (word) VALUES (?);
    """
    cursor.execute(query, (word,))
