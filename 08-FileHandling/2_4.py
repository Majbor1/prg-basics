###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as o_file:
    with open("software_engineer.txt", 'w') as f_file:
        for line in o_file:
            if job_title in line:
                f_file.write(f"{line}")