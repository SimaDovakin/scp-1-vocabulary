from vocabulary.db.decorators import db_query


@db_query
def get_words(cursor):
    query = """
        SELECT word, translation FROM words;
    """
    cursor.execute(query)
    words = cursor.fetchall()
    return words
