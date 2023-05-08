def save_credentials_users(path, users_info):
    with open(path, "wb") as fh:
        for k in users_info.items():
            credentials = k[0] + ':' + k[1] + '\n'
            print(credentials)
            fh.write(credentials.encode())


users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
path = 'hw6-10.txt'
save_credentials_users(path, users_info)