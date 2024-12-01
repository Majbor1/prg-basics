import json

with open('euro.json', 'r') as file:
    content = json.load(file)

for row in content['rates']:
    print(f"Date: {row['effectiveDate']}, Buying rate: {row['bid']}, Selling rate: {row['ask']}")