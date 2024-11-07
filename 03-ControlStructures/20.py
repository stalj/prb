def convert_to_coins(amount):
    coins = [5, 2, 1]
    result = {}
    
    for coin in coins:
        result[coin] = amount // coin
        amount = amount % coin
    
    return result

# Example input
amount = int(input("Enter the amount in PLN: "))
coins = convert_to_coins(amount)

print(f"The amount of PLN {amount} in coins:")
for coin, count in coins.items():
    print(f"{coin} PLN coins: {count}")
