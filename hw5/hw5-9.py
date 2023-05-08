def formatted_numbers():
    new_numbers = []

    for i in range(16):
        if i == 0:
            new_numbers.append('| decimal  |   hex    |  binary  |')
        new_numbers.append('|{:<10}|{:^10x}|{:>10b}|'.format(i, i, i))

    return new_numbers



for el in formatted_numbers():
    print(el)