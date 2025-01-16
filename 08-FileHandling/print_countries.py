###
# Reads from file, line by line
i=1
with open('08-FileHandling\countries.txt', 'r') as file:
    for line in file:
        print(f'{i} {line}')
        i+=1