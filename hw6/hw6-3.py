def read_employees_from_file(path):
    fh = open(path, "r")
    result_list = []
    for k in fh:
        line = k.replace("\n","")
        result_list.append(line)
    fh.close()

    return result_list