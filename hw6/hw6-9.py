def is_equal_string(utf8_string, utf16_string):
    is_eq = None

    decoded_string_8 = (utf8_string.decode('utf-8')).casefold()
    decoded_string_16 = (utf16_string.decode('utf-16')).casefold()
    
    if decoded_string_8 == decoded_string_16:
        is_eq = True
    else:
        is_eq = False

    return is_eq