import re


def find_all_phones(text):
    result = re.findall(r"\+380\([0-9]{2}\)[0-9]{3}\-[0-9]\-[0-9]{3}|\+380\([0-9]{2}\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}", text)
    return result