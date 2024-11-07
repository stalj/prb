def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary if binary else "0"

# Example input
decimal_number = int(input("Enter decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"{decimal_number}(10) = {binary_number}(2)")
