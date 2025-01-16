###
# Saves to a file a list of employees working at a specified position.
###

# File names
employees_file = '08-FileHandling\it_company.csv'
position_file = '08-FileHandling\software_engineer.txt'

# Position
job_title = 'Software Engineer'

# Write selected employees to a file
with open(employees_file, 'r') as input_file:
    with open(position_file, 'w') as output_file:
        for line in input_file:
            if job_title in line:
                output_file.write(line)

print(f"Employees with the position '{job_title}' have been saved to '{position_file}'.")
