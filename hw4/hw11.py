def is_valid_password(password):
    is_valid_pass = True
    
    if len(password) < 8:
        is_valid_pass = False

    for i in range(len(password)):
        if password[i].isupper():
            print("We found Upper symbol ", password[i])
            break
        if (i == len(password)-1) and not password[i].isupper():
            return False
    
    for i in range(len(password)):
        if password[i].islower():
            print("We found Lower symbol ", password[i])
            break
        if (i == len(password)-1) and not password[i].islower():
            return False
        
    for i in range(len(password)):
        print(i)
        if password[i].isnumeric():
            print("We found Numeric symbol ", password[i])
            break
        if i == len(password)-1:
            if password[i].isnumeric() == False:
                print("We didn't find any numbers!")
                return False        
        
    return is_valid_pass

print(is_valid_password('z,rqE*IE'))