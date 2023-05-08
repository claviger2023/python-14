grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    new_students = []
    n = 0
    for k, v in students.items():
        n += 1
        grade_number = grades.get(v)
        new_str = '{:>4}|{:<10}|{:^5}|{:^5}'.format(n, k, v, grade_number)
        new_students.append(new_str)
    return new_students


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)