def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file('countries.txt')

file_lines = file_content.splitlines()

sorted_lines = sorted(file_lines)

for line in sorted_lines:
    print(line)
