current = int(input("Enter current price: "))
previous = int(input("Enter previous: "))
procentage = 100 - (current / previous * 100)

if procentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {procentage}%")