def add_employee_to_file(record, path):
    fh = open(path, "a")
    fh.write(record + "\n")

    fh.close()