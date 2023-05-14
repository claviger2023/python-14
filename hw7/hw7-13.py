def get_employees_by_profession(path, profession):
    with open(path, "r") as fh:
        professions = fh.readlines()
        result_list = []
        for i in professions:
            if i.find(profession) == -1:
                continue
            else:
                i.strip()
                i.rstrip('\n')
                result_list.append(i)
        
        string = ''.join(result_list)
        string = string.replace(profession, '').replace('\n',"").rstrip()

    return string

print(get_employees_by_profession('hw7-13.txt', 'cook'))