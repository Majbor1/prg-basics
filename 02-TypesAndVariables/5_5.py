price = input("Enter price: ")
discount = input("Enter discount %: ")

price = float(price)
discount = int(discount)

discount_p = discount * 0.01
price_w_d = price - (price * discount_p)

reduction = price - price_w_d

print(f"Price: {round(price, 2)}")
print(f"Discount: {discount}%")
print(f"Price with discoubnt: {round(price_w_d, 2)}")
print(f"Reduction: {round(reduction, 2)}")