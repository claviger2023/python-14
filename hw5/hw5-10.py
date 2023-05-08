import re


def find_word(text, word):
    pattern = word
    result = re.search(pattern, text)

    if result == None:
        search_result = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }
    else:
        positions = result.span()
        search_result = {
            'result': True,
            'first_index': positions[0],
            'last_index': positions[1],
            'search_string': result.group(),
            'string': text
        }

    return search_result

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))