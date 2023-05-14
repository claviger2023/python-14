def capital_text(s):
    flag = False
    s = s.strip()
    result = ''

    for i in range(len(s)):
        if i == 0:
            result += s[i].upper()
            continue
        
        if s[i] == '.' or s[i] == '!' or s[i] == '?':
            flag = True
            result += s[i]
            continue

        if flag and s[i] != ' ':
            result += s[i].upper()
            flag = False
            continue
        
        result += s[i]

    return result