from vocabulary.db.decorators import db_query


@db_query
def get_words(cursor):
    query = """
        SELECT word, translation FROM words;
    """
    cursor.execute(query)
    words = cursor.fetchall()
    return words


@db_query
def get_word_description(cursor, word):
    query = """
        SELECT translation FROM words
        WHERE word = :s;
    """
    cursor.execute(query, (word,))
    word_description = cursor.fetchone()
    return word_description[0] if word_description else None
