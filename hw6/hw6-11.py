def get_credentials_users(path):
    with open(path, 'rb') as fh:
        result_credentials = []
        for k in fh:
            result_credentials.append(k.decode().rstrip('\n'))
    return result_credentials

get_credentials_users('hw6-10.txt')