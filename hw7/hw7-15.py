def flatten(data):
    # check if list is empty
    if not(bool(data)):
        return data
 
     # to check instance of list is empty or not
    if isinstance(data[0], list):
 
        # call function with sublist as argument
        return flatten(*data[:1]) + flatten(data[1:])
 
    # call function with sublist as argument
    return data[:1] + flatten(data[1:])