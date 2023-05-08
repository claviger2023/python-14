import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"[\w]+://www[.]{1}[\w]+.[\w]+|[\w]+://[\w]+[.]{1}[\w]+", text)
    for match in iterator:
        result.append(match.group())
    return result