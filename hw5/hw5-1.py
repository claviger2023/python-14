def real_len(text):         
    count = len(text) - text.count("\n") - text.count("\f") - text.count("\r") - text.count("\t") - text.count("\v")

    return count

real_len('Alex\nKdfe23\t\f\v.\r')