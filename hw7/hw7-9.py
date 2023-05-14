def all_sub_lists(data):
    
    if data == []:
        return [[]]

    result_list = [[]]

    for el in data:
        el = [el]
        result_list.append(el)
    
    count = len(data)
    temp_list = []
    
    for i in range(count):
        if i < count-1:
            temp_list = data[i:i+2]
            result_list.append(temp_list)
    
    for i in range(count):
        if i < count-2:
            temp_list = data[i:i+3]
            result_list.append(temp_list)


    result_list.append(data)

    return result_list