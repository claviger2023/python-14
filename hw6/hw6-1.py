def total_salary(path):
  fh = open(path, 'r')
  salaries = 0
  while True:
    line = fh.readline()
    if not line:
      break
    line = line.split(",")
    salaries += float(line[1])
    print(line)

  fh.close()
  
  return salaries

    
path = 'salaries.txt'
print (total_salary(path))