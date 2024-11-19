employees_file = 'it_company.csv'

with open(employees_file) as file:
    content = file.read()
    


file_lines = content.splitlines()

i = 0
a = ""
for line in file_lines:
    if i < 5:
        print(line)
        i += 1
    elif i == 5:
        a = input()
        if a == "":
            i = 0