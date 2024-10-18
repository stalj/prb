number = int(input("enter number:"))
if number > 0:
    print(f'{number} is positive')
elif number < 0:
    print(f'{number} is negative')
elif number==0:
    print(f'{number} is 0')
else: print(" wrong")