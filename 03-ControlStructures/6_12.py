number = int(input("Number of product puchased: "))
price = int(input("Product price: "))

if number > 2:
    amount = (price * 0.75) * (number - 2)

amount += price * 2

print(f"Amount to pay: {amount}")