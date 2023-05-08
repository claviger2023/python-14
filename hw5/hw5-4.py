def is_check_name(fullname, first_name):
    x=fullname.find(first_name)
    if x==0:
        k=True
    else:
        k=False
    return k
    
print(is_check_name('anna tikhonova','jh'))