import re


def find_all_words(text, word):
    pattern = word
    result = re.findall(pattern, text, re.IGNORECASE)

    return result

print(find_all_words(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "pythoN"))    
