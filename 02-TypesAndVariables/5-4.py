def calculate_vat(amount, vat_rate=23):
    vat = amount * (vat_rate / 100)
    return vat

amount = float(input("Enter the amount: "))

vat = calculate_vat(amount)
round_amount=round(amount,2)
round_vat=round(vat,2)

print(f"Amount  : {amount}")
print(f"VAT 23% : {round_vat}")
