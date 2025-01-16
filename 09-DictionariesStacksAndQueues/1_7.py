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

print("PRODUCTS AND QUANTITIES:")
for product, quantity in store.items():
    print(f"{product}: {quantity}")

total_products = sum(store.values())
print("Total number of products in store:", total_products)

