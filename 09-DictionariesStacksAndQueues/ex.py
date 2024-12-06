# Mobile phone dictionary
mobile = {
    "OS": "Android",
    "Brand": "Samsung",
    "Model": "Galaxy S21",
    "Year": 2021,
    "Color": "Phantom Black",
    "Battery Life": "24 hours"
}

# Iterating through the dictionary
for key, value in mobile.items():
    print(f"{key}: {value}")
# 2. Person Dictionary and Modifications
# python
# Копировать код
# Original dictionary
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Displaying specific information
print("Name:", person["name"])
print("Hobby:", person["hobby"])

# Displaying the entire dictionary
print("Original dictionary:", person)

# Making changes
person["surname"] = "Nowak"
person["married"] = not person["married"]
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["work"] = "313131444"

# Displaying modified dictionary
for key, value in person.items():
    print(f"{key}: {value}")
# 3. Array of Country Dictionaries
# python
# Копировать код
# Array of countries with their population
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Italy", "population": 60000000},
    {"name": "Spain", "population": 47000000}
]

# Displaying contents
print("COUNTRY  POPULATION")
for country in countries:
    print(f"{country['name']}   {country['population']}")
# 4. Phone Book Filter by Names Starting with 'D'
# python
# Копировать код
# Phone book dictionary
phone_book = {
    'John': '555-1234',
    'David': '555-5678',
    'Bob': '555-8765',
    'Charlie': '555-4321',
    'Diana': '555-9876',
    'Eve': '555-6543',
    'Frank': '555-3456',
    'Grace': '555-7890',
    'Hank': '555-1111',
    'Ivy': '555-2222',
    'Jack': '555-3333',
    'Daniel': '555-4444',
    'Liam': '555-5555',
    'Mia': '555-6666',
    'Nina': '555-7777',
    'Oscar': '555-8888',
    'Paul': '555-9999',
    'Dominic': '555-1010',
    'Rachel': '555-2020',
    'Sam': '555-3030'
}

# Displaying details of people whose names start with 'D'
print("Contacts whose names start with 'D':")
for name, number in phone_book.items():
    if name.startswith('D'):
        print(f"{name}: {number}")
# 5. Computer Store Products
# python
# Копировать код
# Products dictionary
store = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# Displaying list of products and their quantities
print("PRODUCTS AND QUANTITIES:")
for product, quantity in store.items():
    print(f"{product}: {quantity}")

# Calculating the total number of products
total_products = sum(store.values())
print("Total number of products in store:", total_products)
# Original price list
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# 1. Printing the list of products and prices before the discount
print("Prices before discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

# 2. Calculating the total value of the products before the discount
total_before_discount = sum(price_list.values())
print(f"\nTotal value before discount: ${total_before_discount:.2f}")

# 3. Modifying the price list with a 10% discount
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

# 4. Printing the list of products and prices after the discount
print("\nPrices after 10% discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

# 5. Calculating the total value of the products after the discount
total_after_discount = sum(price_list.values())
print(f"\nTotal value after discount: ${total_after_discount:.2f}")


emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
unique_emails = set(emails)  # Removes duplicates
print(unique_emails)
# 2. Identify Absent Students
# python
# Копировать код
all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = all_students - attended_students  # Difference
print(absent_students)
# 3. Find Spam Emails
# python
# Копировать код
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = emails_received & spam_list  # Intersection
print("Spam emails:", spam_emails)
# 4. Combine Contact Lists and Remove Duplicates
# python
# Копировать код
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = contacts_A | contacts_B  # Union
print("Merged contacts:", merged_contacts)
# 5. Check User Permissions
# python
# Копировать код
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = user_permissions.issubset(required_permissions)  # Check subset
print(has_permissions)  # Will return False because "execute" is missing.





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
