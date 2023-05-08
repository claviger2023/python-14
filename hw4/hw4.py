def split_list(grade):
    sum = 0
    average = 0
    n = 0
    lm = []
    bm = []
    for i in grade:
        n += 1
        sum += i
    try: 
        average = sum / n
    except ZeroDivisionError:
        print("Zero division error")
    for l in grade:
        if l <= average:
            lm.append(l)
        else:
            bm.append(l)
    return lm, bm

numbers = [1, 2, 3, 4, 5]
print(split_list(numbers))
