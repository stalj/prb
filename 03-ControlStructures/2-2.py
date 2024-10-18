 ###
    # A program for checking clothing sizes
    # S: Small size, M: Medium size, L: Large size
    # XL: Extra large size or Incorrect symbol (if entered symbol
    # dirrerent than S, M, L, XL)
    #
size = input('Enter size symbol: ')

if size == 'S':
        print(f'{size}: Small size')
elif size == 'M':
        print(f'{size}: Medium size')
elif size == 'L':
        print(f'{size}: Large size')
elif size == 'XL':
        print(f'{size}: Extra large size')        
else:
        print("YOU ENTERED WRONG SIMBOL")
