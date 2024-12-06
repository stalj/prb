







# python
# Копировать код

# 5. Check User Permissions
# python
# Копировать код
 # Will return False because "execute" is missing.





def brackets_ok(expression):
    # Dictionary to match opening and closing brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    stack = []  # Stack to store opening brackets

    # Iterate through the expression
    for char in expression:
        if char in "({[":  # If opening bracket, push to stack
            stack.append(char)
        elif char in ")}]":  # If closing bracket
            if not stack or stack.pop() != bracket_pairs[char]:
                return False  # Stack empty or mismatch

    return len(stack) == 0  # True if stack is empty (all brackets matched)

# Test expressions
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # Brackets okay
expression2 = "[(2+3]/4)"                 # Brackets not correct
expression3 = "(2-3*4+(5/6)"              # Brackets not correct

# Check and print results
for i, expression in enumerate([expression1, expression2, expression3], 1):
    if brackets_ok(expression):
        print(f"Expression {i}: Brackets are correct")
    else:
        print(f"Expression {i}: Brackets are NOT correct")



def convert_to_binary(number):
    stack = []  # Stack to store remainders

    # Perform division by 2 and collect remainders
    while number > 0:
        remainder = number % 2
        stack.append(remainder)
        number //= 2

    # Construct binary number by popping from stack
    binary_number = ""
    while stack:
        binary_number += str(stack.pop())

    return binary_number

# Input and conversion
natural_number = 18
binary_number = convert_to_binary(natural_number)

# Print the result
print(f"Natural number: {natural_number}")
print(f"Binary number: {binary_number}")


import queue

# Creates a queue of files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
    
    if menu == '1':  # Add a file to the queue
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)  # Add the file to the end of the queue
        print(f'File "{file_name}" has been added to the print queue.')

    elif menu == '2':  # Print a file
        if not files_to_print.empty():  # Check if the queue is not empty
            file_to_print = files_to_print.get()  # Get the next file from the queue
            print(f'File "{file_to_print}" is currently being printed. Please wait!')
        else:
            print('The print queue is empty. No files to print.')

    elif menu == '0':  # Exit the program
        print('Exiting the program. Goodbye!')
        break

    else:  # Invalid menu option
        print('Invalid option. Please try again.')
