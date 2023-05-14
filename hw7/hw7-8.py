def token_parser(s):
    result = []
    temp = ''
    flag = False
    for k in s:
        if k == ' ':
            if flag:
                result.append(temp)
                flag = False
                temp = ''
            continue
        elif k == '+' or k == '-' or k == '/' or k == '*' or k == '(' or k == ')':
            if flag:
                result.append(temp)
                flag = False
                temp = ''
            result.append(k)
        elif k.isnumeric():
            flag = True
            temp = temp + k
    if temp != '':
        result.append(temp)
    
    return result
