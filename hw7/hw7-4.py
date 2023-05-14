def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    
    for i in range(len(s)):
        if s[i].isnumeric():
            continue
        elif i == 0 and (s[i] == '+' or s[i] == '-'):
            continue
        else:
            return False

    return True