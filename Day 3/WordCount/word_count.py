def words(phrase):
    """
        This function returns a dictionary containing distinct words from the phrase argument as keys and the number 
        of times they appear as the values 
    """

    the_words = phrase.split()
    distinct = {}
    for a_word in the_words:
        if a_word not in distinct:
            try:
                distinct[int(a_word)] = the_words.count(a_word)
            except ValueError:
                distinct[a_word] = the_words.count(a_word)
    return distinct

