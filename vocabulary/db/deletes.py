from vocabulary.db.decorators import db_query


@db_query
def delete_word(cursor, word):
    query = """
        DELETE FROM words
        WHERE word = :s;
    """
    cursor.execute(query, (word,))
