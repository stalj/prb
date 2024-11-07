# Using a while loop instead of a for loop to display the keyboard layout

i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f"{i + j}", end=" ")
        j += 1
    print()
    i -= 3
