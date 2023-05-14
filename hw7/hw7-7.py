def data_preparation(list_data):
    result_list = []

    for list in list_data:
        if len(list) > 2:
            list.sort()
            list.pop(0)
            list.pop(len(list)-1)
            for v in list:
                result_list.append(v)
        else:
            for m in list:
                result_list.append(m)

    result_list.sort()
    result_list.reverse()
    
    return result_list

raw_list = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
print(data_preparation(raw_list))