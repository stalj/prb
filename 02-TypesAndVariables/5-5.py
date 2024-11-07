discount = int(input("enter discount:"))
price = int(input("enter price:"))

dic_price= price - (price*discount/100)
 
print(f'dickount = {discount}, price = {price}, discounted price = {dic_price:.2f} ')