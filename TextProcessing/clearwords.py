import string


def clear_words(text):
    if type(text) != str:
        raise "Not a valid type for conversion"

    new_str = text.translate(None, string.punctuation).lower().split()
    for ind, item in enumerate(new_str):
        try:
            int(item)
            new_str.pop(ind)
        except ValueError:
            pass
    return new_str
