import json

product = {}


name = input("Enter name: ")
price = float(input("Enter price: "))
paid = input("Paid (yes/no): ")
if paid == 'yes':
    is_paid = True
elif paid == 'no':
    is_paid = False
else:
    is_paid = False

product['name'] = name
product['price'] = round(price, 2)
product['paid'] = is_paid
with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

    
    


