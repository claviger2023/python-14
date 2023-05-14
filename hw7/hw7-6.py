def solve_riddle(riddle, word_length, start_letter, reverse=False):
    pos = riddle.find(start_letter)
    if pos == -1:
        return ''
    
    word = ''
    if reverse:
        start = pos - word_length
        while pos > start:
            word += riddle[pos]
            pos -= 1

    else:
        for i in range(len(riddle)):
            if i >= pos and word_length > 0:
                word += riddle[i]
                word_length -= 1
            elif word_length == 0:
                break
    
    return word
