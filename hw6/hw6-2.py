def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for department in employee_list:
        for i in range(len(department)):
            employee = department[i] + '\n'
            fh.write(employee)
    fh.close()

employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = 'hw6-2.txt'
write_employees_to_file(employee_list, path)

fh2 = open(path, 'r')
print(fh2.read())