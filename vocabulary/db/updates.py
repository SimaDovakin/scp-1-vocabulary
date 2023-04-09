from vocabulary.db.decorators import db_query


@db_query
def update_word_description(cursor, word, description):
    query = """
        UPDATE words
        SET translation = ?
        WHERE word = ?;
    """
    cursor.execute(query, (description, word))
