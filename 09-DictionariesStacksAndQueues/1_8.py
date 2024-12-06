# The data below contains a price list of items from a clothing store along with their prices.
#  Due to a seasonal sale, the store is reducing the price of each item by 10%. Write a program that:

# prints a list of products and their prices before the discount
# prints the total value of the products before the discount
# modifies the price list according to the discount (round prices to two decimal places)
# prints a list of products and their prices after the 10% discount
# prints the total value of the products after the discount



price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Prices before discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")


total_before_discount = sum(price_list.values())
print(f"\nTotal value before discount: ${total_before_discount:.2f}")


for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)


print("\nPrices after 10% discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")


total_after_discount = sum(price_list.values())
print(f"\nTotal value after discount: ${total_after_discount:.2f}")