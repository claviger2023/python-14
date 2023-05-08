from random import randint


def get_random_password():
    password = ''
    for _ in range(8):
        random_num = randint(40, 126)
        password = password + chr(random_num)
    return password

