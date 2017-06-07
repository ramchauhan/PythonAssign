def getwords(text):
    """
    Method to parse a string and return the words
    Args:
        text (str): text which needs to be parse
    return:
        list of words after parsing
    """
    if type(text) != str:
        raise "Not a valid type for processing"

    return text.split()
