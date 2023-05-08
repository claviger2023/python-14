def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    check_result = False

    if not space_around:
        for s_word in spam_words:
            if text.find(s_word) != -1:
                check_result = True
                break
    else:
        for s_word in spam_words:
            if text.find(s_word) == 0:
                check_result = True
                break
            elif text.find(s_word) == -1:
                continue
            else:
                pos_start = text.find(s_word)
                pos_end = pos_start + len(s_word)
                if text[pos_start-1] == ' ' and (text[pos_end] == ' ' or text[pos_end] == '.'):
                    check_result = True
                    break

    return check_result