def f(list):
    counter = 0
    for key, value in list.items():
        print(f"{key}: {value}")
        counter += value

    print(f"Total value: {round(counter, 2)}")

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print("Before")
f(price_list)

for key, value in price_list.items():
    price_list[key] = round(value * 0.9, 2)


print("After")
f(price_list)