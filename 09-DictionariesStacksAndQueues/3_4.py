def convert_to_binary(number):
    stack = [] 

    while number > 0:
        remainder = number % 2
        stack.append(remainder)
        number //= 2

  
    binary_number = ""
    while stack:
        binary_number += str(stack.pop())

    return binary_number


natural_number = 18
binary_number = convert_to_binary(natural_number)


print(f"Natural number: {natural_number}")
print(f"Binary number: {binary_number}")