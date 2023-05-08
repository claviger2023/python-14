import shutil
import os


def create_backup(path, file_name, employee_residence):
    full_path = path + '/' + file_name
    with open(full_path, "wb") as fh:
        for key, value in employee_residence.items():
            line = key + ' ' + value + '\n'
            fh.write(line.encode())
        
        archive_name = shutil.make_archive('backup_folder', 'zip', 'folder')

    return archive_name