import re


def replace_spam_words(text, spam_words):
    result_text = text
    for spam_word in spam_words:
        replace_text = ''
        for i in spam_word:
            replace_text = replace_text + '*'
        
        results = re.findall(spam_word, text, re.IGNORECASE)
        for v in results:
            result_text = re.sub(v, replace_text, result_text)
  

    return result_text

print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))