###
# Prints employees employed in a specified position.
#

# Employee List
file_name = '08-FileHandling\it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
   for line in file:
      if job_title in line:
         print(line)