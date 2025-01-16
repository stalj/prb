def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('08-FileHandling\car_park.txt')
file_lines = file_content.splitlines()


total = 0
for line in file_lines:
   total += int(line)

print('Total cars parked:', total)