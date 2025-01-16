def print_lottery_coupon():
    for row in range(1, 8):  # There are 7 rows
        for col in range(row, 50, 7):  # Each column number starts at `row` and increments by 7
            print(f"{col:2}", end=" ")
        print()  # Newline after each row

# Print the lottery coupon
print_lottery_coupon()
