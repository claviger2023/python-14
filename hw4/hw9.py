def is_valid_pin_codes(pin_codes):
    if len(pin_codes) <= 1:
        return False
    is_valid = True
    
    for p in pin_codes:
        if len(p) != 4:
            return False
    
    for i in range(len(pin_codes)):
        if i != 0:
            if pin_codes[i] == pin_codes[0]:
                return False
        
    for m in pin_codes:
        if len(m) != 4:
            return False
        for s in m:
            if not s.isnumeric():
                return False 

    return is_valid

is_valid_pin_codes(['1101', '9034', '0011', '1101'])